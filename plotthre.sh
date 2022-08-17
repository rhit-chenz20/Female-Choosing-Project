declare date="Aug14"
declare c=0
declare max=40

mkdir ../result/${date}/plot/Threshold/mating_length
mkdir ../result/${date}/plot/Threshold/male_sigma
mkdir ../result/${date}/plot/Threshold/fitness_function
mkdir ../result/${date}/plot/Threshold/cost

for MS in 1
do
    for FS in 10
    do
        for FM in 1
        do
            for COST in 0
            do
                for FIT in 0
                do
                        # ploting mating length

                        let "c+=1"
                        python3 plot.py -inf ../result/${date}/CSV/Threshold/ml_*_ms_${MS}_fit_${FIT}_cost_${COST}_*.csv -out ../result/${date}/plot/Threshold/mating_length/ms_${MS}_fit_${FIT}_cost_${COST}_1 -t 0 -ing ../result/${date}/CSV/Threshold/last_ml_*_ms_${MS}_fit_${FIT}_cost_${COST}_*.csv
                        echo "finished plotting $c"
                        
                        if ((c>$max))
                            then
                                wait
                                let "c=0"
                            fi


                done
            done
        done
    done            
done
                    
echo "finished plotting"