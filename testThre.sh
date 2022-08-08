declare date="Aug8"
mkdir "../result"
mkdir "../result/$date"
mkdir "../result/${date}/CSV"
mkdir "../result/$date/plot"
mkdir "../result/${date}/CSV/Threshold"
mkdir "../result/$date/plot/Threshold"

for COST in 0 1 2
do
    for V in {1..10}
    do
        let "c+=1"
        echo "running $c"
        # pwd
        # python ~/Documents/GitHub/Female-Choosing-Project/run.py -ml 10 -ms 3 -fsigma 3 -fmu 5 -fit 2 -fn "../result/CSV/${date}/fit_2_$V" -ft 0 -sel 0 -max 5 -fs 3
        python3 run.py -ml 10 -ms 3 -fsigma 3 -fmu 5 -fit 0 -fn "../result/${date}/CSV/Threshold/cost_${COST}_$V" -ft 0 -sel 0 -max 3000 -fs 3 -c $COST
        if ((c>5))
            then
                wait
                let "c=0"
            fi
    
    done
done

let "c+=1"
echo "plotting $c"
# python ~/Documents/GitHub/Female-Choosing-Project/plot.py -inf ../result/CSV/${date}/Threshold/fit_2_*.csv -out ../result/plot/${date}/threshold/fitness_function/LSP -t 0
mkdir ../result/${date}/plot/Threshold/cost
python3 plot.py -inf ../result/${date}/CSV/Threshold/cost_*_*.csv -out ../result/${date}/plot/Threshold/cost/cost_test_max_3000 -t 0
echo "finished $c"