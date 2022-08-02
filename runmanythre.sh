#!/bin/bash
declare date="July28"
# # conda activate female-mating
# count = 0
# # maleMu = 5
# # 4 different mating length, aka how many chances a female gets for mating
# for ML in 1 5 10
# do
#     # 3 different male sigma
#     for MS in 1 10 100
#     do
#         # 3 female figma
#         for SR in 0.01 1 10
#         do
#             #10 trails for each set of parameters
#             for V in {1..10}
#             do
#                 python /Users/andrea/Documents/GitHub/Female-Choosing-Project/run.py -ml $ML -ms $MS -fsigma $SR -fmu 5 -fit 1 -fn "ml_${ML}_ms_${MS}_mus_${MuS}_fsigma_${SR}_$V"
#                 # pids[${count}]=$!
#                 echo "running $count"
#                 let "count+=1"
#             done
#         done
#     done
# done

# for pid in ${pids[*]}
# do
#     wait $pid
# done

# c=1
# # 4 different mating length, aka how many chances a female gets for mating
# for ML in 1 5 10
# do
#     # 3 different male sigma
#     for MS in 1 10 100
#     do
#         # 3 female figma
#         for SR in 0.01 1 10
#         do
#             python /Users/andrea/Documents/GitHub/Female-Choosing-Project/plot.py -in CSVResultFiles/June28/ml_${ML}_ms_${MS}_mus__fsigma_${SR}_*.csv -out ml_${ML}_ms_${MS}_mus__fsigma_${SR}
#             echo "plotting $c"
#             let "c+=1"
           
#         done
#     done
# done

# echo "finished"

# for SEL in 0 1
# do
#     for V in {1..10}
#     do
#         let "c+=1"
#         echo "running $c"
#         python /Users/andrea/Documents/GitHub/Female-Choosing-Project/run.py -ml 10 -ms 3 -fsigma 3 -fmu 5 -fit 0 -fn "thre_sel_${SEL}_$V" -ft 0 -sel $SEL -d "July26"
#     done
# done

# let "c+=1"
# echo "plotting $c"
# python /Users/andrea/Documents/GitHub/Female-Choosing-Project/plot.py -inf CSVResultFiles/July26/thre_sel${SEL}_*.csv -outfolder July26/threshold/selection -out selection -t 0
# echo "finished $c"



# for SEL in 0 1
# do
#     for MS in 1 5 10
#     do
#         for FS in 1 5 10
#         do
#             for FM in 1 5 10
#             do
#                 for COST in 0 0.5 1
#                 do
#                     for FIT in 0 1 2
#                     do
#                         for V in {1..10}
#                         do
#                             let "c+=1"
#                             echo "running $c"
#                             python /Users/andrea/Documents/GitHub/Female-Choosing-Project/run.py -ml 20 -ms $MS -fsigma $FS -fmu $FM -fit $FIT -fn "sel_${SEL}_ms_${MS}_fs_${FS}_fmu_${FM}_fit_${FIT}_cost_${COST}_$V" -ft 0 -sel $SEL -d ${date} -c $COST
#                         done
#                     done
#                 done
#             done
#         done
#     done              
# done

for SEL in 0 1
do
    for MS in 1 5 10
    do
        for FS in 1 5 10
        do
            for FM in 1 5 10
            do
                for COST in 0 0.5 1
                do
                    for FIT in 0 1 2
                    do
                        # # ploting selection
                        # let "c+=1"
                        # echo "plotting $c"
                        # python /Users/andrea/Documents/GitHub/Female-Choosing-Project/plot.py -inf CSVResultFiles/${date}/Threshold/sel_*_ms_${MS}_fs_${FS}_fmu_${FM}_fit_${FIT}_cost_${COST}_*.csv -outfolder ${date}/threshold/selection -out ms_${MS}_fs_${FS}_fmu_${FM}_fit_${FIT}_cost_${COST} -t 0
                        # echo "finished $c"
                        # # ploting male sigma
                        # let "c+=1"
                        # echo "plotting $c"
                        # python /Users/andrea/Documents/GitHub/Female-Choosing-Project/plot.py -inf CSVResultFiles/${date}/Threshold/sel_${SEL}_ms_*_fs_${FS}_fmu_${FM}_fit_${FIT}_cost_${COST}_*.csv -outfolder ${date}/threshold/male_sigma -out sel_${SEL}_fs_${FS}_fmu_${FM}_fit_${FIT}_cost_${COST} -t 0
                        # echo "finished $c"
                        # # ploting female sigma
                        # let "c+=1"
                        # echo "plotting $c"
                        # python /Users/andrea/Documents/GitHub/Female-Choosing-Project/plot.py -inf CSVResultFiles/${date}/Threshold/sel_${SEL}_ms_${MS}_fs_*_fmu_${FM}_fit_${FIT}_cost_${COST}_*.csv -outfolder ${date}/threshold/female_sigma -out sel_${SEL}_ms_${MS}_fmu_${FM}_fit_${FIT}_cost_${COST} -t 0
                        # echo "finished $c"
                        # # ploting female mu
                        # let "c+=1"
                        # echo "plotting $c"
                        # python /Users/andrea/Documents/GitHub/Female-Choosing-Project/plot.py -inf CSVResultFiles/${date}/Threshold/sel_${SEL}_ms_${MS}_fs_${FS}_fmu_*_fit_${FIT}_cost_${COST}_*.csv -outfolder ${date}/threshold/female_mean -out sel_${SEL}_ms_${MS}_fs_${FS}_fit_${FIT}_cost_${COST} -t 0
                        # echo "finished $c"
                        # # ploting fitness function
                        # let "c+=1"
                        # echo "plotting $c"
                        # python /Users/andrea/Documents/GitHub/Female-Choosing-Project/plot.py -inf CSVResultFiles/${date}/Threshold/sel_${SEL}_ms_${MS}_fs_${FS}_fmu_${FM}_fit_*_cost_${COST}_*.csv -outfolder ${date}/threshold/fitness_function -out sel_${SEL}_ms_${MS}_fs_${FS}_fmu_${FM}_cost_${COST} -t 0
                        # echo "finished $c"
                        # ploting cost
                        let "c+=1"
                        echo "plotting $c"
                        python /Users/andrea/Documents/GitHub/Female-Choosing-Project/plot.py -inf CSVResultFiles/${date}/sel_${SEL}_ms_${MS}_fs_${FS}_fmu_${FM}_fit_${FIT}_cost_*_*.csv -outfolder ${date}/threshold/cost -out sel_${SEL}_ms_${MS}_fs_${FS}_fmu_${FM}_fit_${FIT} -t 0
                        echo "finished $c"
                    done
                done
            done
        done
    done            
done
                        # let "c+=1"
                        # echo "plotting $c"
                        # python /Users/andrea/Documents/GitHub/Female-Choosing-Project/plot.py -inf CSVResultFiles/${date}/Threshold/sel_0_ms_*_fs_1_fmu_1_fit_1_cost_1_*.csv -outfolder ${date}/threshold/male_sigma -out sel_0_fs_1_fmu_1_fit_1_cost_1 -t 0
                        # echo "finished $c"
                        
                        # let "c+=1"
                        # echo "plotting $c"
                        # python /Users/andrea/Documents/GitHub/Female-Choosing-Project/plot.py -inf CSVResultFiles/${date}/Threshold/sel_0_ms_1_fs_1_fmu_1_fit_1_cost_1_*.csv -outfolder ${date}/threshold/male_sigma -out ms_1 -t 0
                        # echo "finished $c"
                        
                        # let "c+=1"
                        # echo "plotting $c"
                        # python /Users/andrea/Documents/GitHub/Female-Choosing-Project/plot.py -inf CSVResultFiles/${date}/Threshold/sel_0_ms_5_fs_1_fmu_1_fit_1_cost_1_*.csv -outfolder ${date}/threshold/male_sigma -out ms_5 -t 0
                        # echo "finished $c"
                        
                        # let "c+=1"
                        # echo "plotting $c"
                        # python /Users/andrea/Documents/GitHub/Female-Choosing-Project/plot.py -inf CSVResultFiles/${date}/Threshold/sel_0_ms_10_fs_1_fmu_1_fit_1_cost_1_*.csv -outfolder ${date}/threshold/male_sigma -out ms_10 -t 0
                        # echo "finished $c"                        