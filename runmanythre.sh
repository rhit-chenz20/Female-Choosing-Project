#!/bin/bash
declare date="Aug8"
mkdir "../result"
mkdir "../result/$date"
mkdir "../result/${date}/CSV"
mkdir "../result/$date/plot"
mkdir "../result/${date}/CSV/Threshold"
mkdir "../result/$date/plot/Threshold"

declare c=0
declare count=0
declare max=40


for MS in 1 5 10
do
    for FS in 1 5 10
    do
        for FM in 1 5 10
        do
            for COST in 0 1 3
            do
                for FIT in 0 1 2
                do
                    for ML in 1 5 10 20
                    do
                        for V in {1..10}
                        do
                            let "count+=1"
                            echo "running $count"

                            python3 run.py -ml $ML -ms $MS -fsigma $FS -fmu $FM -fit $FIT -fn "../result/${date}/CSV/Threshold/ml_${ML}_ms_${MS}_fs_${FS}_fmu_${FM}_fit_${FIT}_cost_${COST}_$V" -ft 0 -sel 0 -c $COST -max 3000 &
                            if ((count>$max))
                            then
                                wait
                                let "count=0"
                            fi
                        done
                    done
                done
            done
        done
    done
done              


for MS in 1 5 10
do
    for FS in 1 5 10
    do
        for FM in 1 5 10
        do
            for COST in 0 1 3
            do
                for FIT in 0 1 2
                do
                    for ML in 1 5 10 20
                    do
                        # ploting mating length
                        mkdir ../result/${date}/plot/Threshold/mating_length
                        let "c+=1"
                        python3 plot.py -inf ../result/${date}/CSV/Threshold/ml_*_ms_${MS}_fs_${FS}_fmu_${FM}_fit_${FIT}_cost_${COST}_*.csv -out ../result/${date}/plot/Threshold/mating_length/ms_${MS}_fs_${FS}_fmu_${FM}_fit_${FIT}_cost_${COST} -t 0 &
                        echo "finished plotting $c"
                        
                        if ((c>$max))
                            then
                                wait
                                let "c=0"
                            fi

                        # ploting male sigma
                        mkdir ../result/${date}/plot/Threshold/male_sigma
                        let "c+=1"
                        python3 plot.py -inf ../result/${date}/CSV/Threshold/ml_${ML}_ms_*_fs_${FS}_fmu_${FM}_fit_${FIT}_cost_${COST}_*.csv -out ../result/${date}/plot/Threshold/male_sigma/ml_${ML}_fs_${FS}_fmu_${FM}_fit_${FIT}_cost_${COST} -t 0 &
                        echo "finished plotting $c"
                        if ((c>$max))
                            then
                                wait
                                let "c=0"
                            fi

                        # ploting female sigma
                        mkdir ../result/${date}/plot/Threshold/female_sigma
                        let "c+=1"
                        python3 plot.py -inf ../result/${date}/CSV/Threshold/ml_${ML}_ms_${MS}_fs_*_fmu_${FM}_fit_${FIT}_cost_${COST}_*.csv -out ../result/${date}/plot/Threshold/female_sigma/ml_${ML}_ms_${MS}_fmu_${FM}_fit_${FIT}_cost_${COST} -t 0 &
                        echo "finished plotting $c"
                        if ((c>$max))
                            then
                                wait
                                let "c=0"
                            fi

                        # ploting female mu
                        mkdir ../result/${date}/plot/Threshold/female_mean
                        let "c+=1"
                        python3 plot.py -inf ../result/${date}/CSV/Threshold/ml_${ML}_ms_${MS}_fs_${FS}_fmu_*_fit_${FIT}_cost_${COST}_*.csv -out ../result/${date}/plot/Threshold/female_mean/ml_${ML}_ms_${MS}_fs_${FS}_fit_${FIT}_cost_${COST} -t 0 &
                        echo "finished plotting $c"
                        if ((c>$max))
                            then
                                wait
                                let "c=0"
                            fi

                        # ploting fitness function
                        mkdir ../result/${date}/plot/Threshold/fitness_function
                        let "c+=1"
                        python3 plot.py -inf ../result/${date}/CSV/Threshold/ml_${ML}_ms_${MS}_fs_${FS}_fmu_${FM}_fit_*_cost_${COST}_*.csv -out ../result/${date}/plot/Threshold/fitness_function/ml_${ML}_ms_${MS}_fs_${FS}_fmu_${FM}_cost_${COST} -t 0 &
                        echo "finished plotting $c"
                        if ((c>$max))
                            then
                                wait
                                let "c=0"
                            fi

                        # ploting cost
                        mkdir ../result/${date}/plot/Threshold/cost
                        let "c+=1"
                        python3 plot.py -inf ../result/${date}/CSV/Threshold/ml_${ML}_ms_${MS}_fs_${FS}_fmu_${FM}_fit_${FIT}_cost_*_*.csv -out ../result/${date}/plot/Threshold/cost/ml_${ML}_ms_${MS}_fs_${FS}_fmu_${FM}_fit_${FIT} -t 0 &
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
done
                    