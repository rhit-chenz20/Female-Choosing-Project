declare date="Aug14"
declare c=0
declare max=40

mkdir ../result/${date}/plot/Learning/mating_length
mkdir ../result/${date}/plot/Learning/male_sigma
mkdir ../result/${date}/plot/Learning/fitness_function
mkdir ../result/${date}/plot/Learning/cost

mkdir ../result/${date}/plot/Threshold/mating_length
mkdir ../result/${date}/plot/Threshold/male_sigma
mkdir ../result/${date}/plot/Threshold/fitness_function
mkdir ../result/${date}/plot/Threshold/cost

for MS in 1 5 10
do
    for FS in 10
    do
        for FM in 1
        do
            for COST in 0 1 3
            do
                for FIT in 0 1 2
                do
                    for ML in 1 3 5 10 20
                    do
                        # ploting mating length

                        let "c+=1"
                        python3 plot.py -inf ../result/${date}/CSV/Learning/ml_*_ms_${MS}_fit_${FIT}_cost_${COST}_*.csv -out ../result/${date}/plot/Learning/mating_length/ms_${MS}_fit_${FIT}_cost_${COST} -t 1 -ing ../result/${date}/CSV/Learning/last_ml_*_ms_${MS}_fit_${FIT}_cost_${COST}_*.csv &

                        let "c+=1"
                        python3 plot.py -inf ../result/${date}/CSV/Threshold/ml_*_ms_${MS}_fit_${FIT}_cost_${COST}_*.csv -out ../result/${date}/plot/Threshold/mating_length/ms_${MS}_fit_${FIT}_cost_${COST} -t 0 -ing ../result/${date}/CSV/Threshold/last_ml_*_ms_${MS}_fit_${FIT}_cost_${COST}_*.csv &
                        
                        if ((c>$max))
                            then
                                wait
                                let "c=0"
                            fi

                        # ploting male sigma

                        let "c+=1"
                        python3 plot.py -inf ../result/${date}/CSV/Learning/ml_${ML}_ms_*_fit_${FIT}_cost_${COST}_*.csv -out ../result/${date}/plot/Learning/male_sigma/ml_${ML}_fit_${FIT}_cost_${COST} -t 1 -ing ../result/${date}/CSV/Learning/last_ml_${ML}_ms_*_fit_${FIT}_cost_${COST}_*.csv &
                        let "c+=1"
                        python3 plot.py -inf ../result/${date}/CSV/Threshold/ml_${ML}_ms_*_fit_${FIT}_cost_${COST}_*.csv -out ../result/${date}/plot/Threshold/male_sigma/ml_${ML}_fit_${FIT}_cost_${COST} -t 0 -ing ../result/${date}/CSV/Threshold/last_ml_${ML}_ms_*_fit_${FIT}_cost_${COST}_*.csv &

                        if ((c>$max))
                            then
                                wait
                                let "c=0"
                            fi

                        # ploting fitness function

                        let "c+=1"
                        python3 plot.py -inf ../result/${date}/CSV/Learning/ml_${ML}_ms_${MS}_fit_*_cost_${COST}_*.csv -out ../result/${date}/plot/Learning/fitness_function/ml_${ML}_ms_${MS}_cost_${COST} -t 1 -ing ../result/${date}/CSV/Learning/last_ml_${ML}_ms_${MS}_fit_*_cost_${COST}_*.csv &
                        let "c+=1"
                        python3 plot.py -inf ../result/${date}/CSV/Threshold/ml_${ML}_ms_${MS}_fit_*_cost_${COST}_*.csv -out ../result/${date}/plot/Threshold/fitness_function/ml_${ML}_ms_${MS}_cost_${COST} -t 0 -ing ../result/${date}/CSV/Threshold/last_ml_${ML}_ms_${MS}_fit_*_cost_${COST}_*.csv &
                        
                        
                        if ((c>$max))
                            then
                                wait
                                let "c=0"
                            fi

                        # ploting cost

                        let "c+=1"
                        python3 plot.py -inf ../result/${date}/CSV/Learning/ml_${ML}_ms_${MS}_fit_${FIT}_cost_*_*.csv -out ../result/${date}/plot/Learning/cost/ml_${ML}_ms_${MS}_fit_${FIT} -t 1 -ing ../result/${date}/CSV/Learning/last_ml_${ML}_ms_${MS}_fit_${FIT}_cost_*_*.csv &
                        let "c+=1"
                        python3 plot.py -inf ../result/${date}/CSV/Threshold/ml_${ML}_ms_${MS}_fit_${FIT}_cost_*_*.csv -out ../result/${date}/plot/Threshold/cost/ml_${ML}_ms_${MS}_fit_${FIT} -t 0 -ing ../result/${date}/CSV/Threshold/last_ml_${ML}_ms_${MS}_fit_${FIT}_cost_*_*.csv &
                        
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
done
                    
echo "finished plotting"