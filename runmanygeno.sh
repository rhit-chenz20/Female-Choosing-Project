# !/bin/bash
declare date="July20"
# # maleMu = 5
# # 2 fitness function (0-average, 1-lowest)
# for FIT in 0 
# #1
# do
#     # 2 selection percentage
#     for PER in 0.5
#     #0.1
#     do
#         # 3 different male sigma
#         for MS in 1 
#         #10 50
#         do                    
#             # 3 female mu
#             for FM in 5
#             #-5 15
#             do

#                 for FSIGMA in 1 
#                 #10 50
#                 do
#                     # 3 female memory
#                     for ME in 0 5 10 20 50
#                     do

#                         for ML in 1 5 10 20 50
#                         do
#                             #10 trails for each set of parameters
#                             for V in {1..10}
#                             do
#                                 python /Users/andrea/Documents/GitHub/Female-Choosing-Project/run.py -ml ${ML} -ms ${MS} -fsigma $FSIGMA -fmu $FM -fit 1 -fn "ml_${ML}_ms_${MS}_fsigma_${FSIGMA}_fmu_${FM}_me_${ME}_selper_${PER}_fit_${FIT}_$V" -ft 1 -memol ${ME} -per ${PER} -fit ${FIT}
#                                 # pids[${count}]=$!
#                                 let "count+=1"
#                                 echo "running $count"
#                             done
#                         done
#                     done
#                 done
#             done
#         done
#     done
# done

# # for pid in ${pids[*]}
# # do
# #     wait $pid
# # done

# c=0

# # plot mating length
# # python /Users/andrea/Documents/GitHub/Female-Choosing-Project/plot.py -inf CSVResultFiles/July8/ms_1_fsigma_1_fmu_*_me_0_*.csv -out ms_1_fsigma_1_fmu_${FM}_me_${ME} -ing CSVResultFiles/July8/geno_ms_${MS}_fsigma_${MS}_fmu_${FM}_me_${ME}_*.csv

# # maleMu = 5
# # mating length
# for FIT in 0 
# #1
# do
#     # 2 selection percentage
#     for PER in 0.5
#     #0.1
#     do
#         # 3 different male sigma
#         for MS in 1 
#         #10 50
#         do                    
#             # 3 female mu
#             for FM in 5 
#             #-5 15
#             do

#                 for FSIGMA in 1 
#                 #10 50
#                 do
#                     # 3 female memory
#                     for ME in 0 5 
#                     #10 20 50
#                     do

#                         for ML in 1 5 10 20 50
#                         do
#                             # fitness function
#                             python /Users/andrea/Documents/GitHub/Female-Choosing-Project/plot.py -inf CSVResultFiles/July8/ml_${ML}_ms_${MS}_fsigma_${FSIGMA}_fmu_${FM}_me_${ME}_selper_${PER}_fit_*_*.csv -outfolder fitness_function -out ml_${ML}_ms_${MS}_fsigma_${FSIGMA}_fmu_${FM}_me_${ME}_selper_${PER} -ing CSVResultFiles/July8/geno_ml_${ML}_ms_${MS}_fsigma_${FSIGMA}_fmu_${FM}_me_${ME}_selper_${PER}_fit_*_*.csv
#                             let "c+=1"
#                             echo "ploting $c"
#                             # selection percent
#                             python /Users/andrea/Documents/GitHub/Female-Choosing-Project/plot.py -inf CSVResultFiles/July8/ml_${ML}_ms_${MS}_fsigma_${FSIGMA}_fmu_${FM}_me_${ME}_selper_*_fit_${FIT}_*.csv -outfolder selection_percent -out ml_${ML}_ms_${MS}_fsigma_${FSIGMA}_fmu_${FM}_me_${ME}_fit_${FIT} -ing CSVResultFiles/July8/geno_ml_${ML}_ms_${MS}_fsigma_${FSIGMA}_fmu_${FM}_me_${ME}_selper_*_fit_${FIT}_*.csv
#                             let "c+=1"
#                             echo "ploting $c"
#                             # memory length
#                             python /Users/andrea/Documents/GitHub/Female-Choosing-Project/plot.py -inf CSVResultFiles/July8/ml_${ML}_ms_${MS}_fsigma_${FSIGMA}_fmu_${FM}_me_*_selper_${PER}_fit_${FIT}_*.csv -outfolder memory_length -out ml_${ML}_ms_${MS}_fsigma_${FSIGMA}_fmu_${FM}_selper_${PER}_fit_${FIT} -ing CSVResultFiles/July8/geno_ml_${ML}_ms_${MS}_fsigma_${FSIGMA}_fmu_${FM}_me_*_selper_${PER}_fit_${FIT}_*.csv
#                             let "c+=1"
#                             echo "ploting $c"
#                             # female sigma
#                             python /Users/andrea/Documents/GitHub/Female-Choosing-Project/plot.py -inf CSVResultFiles/July8/ml_${ML}_ms_${MS}_fsigma_*_fmu_${FM}_me_${ME}_selper_${PER}_fit_${FIT}_*.csv -outfolder female_sigma -out ml_${ML}_ms_${MS}_fmu_${FM}_me_${ME}_selper_${PER}_fit_${FIT} -ing CSVResultFiles/July8/geno_ml_${ML}_ms_${MS}_fsigma_*_fmu_${FM}_me_${ME}_selper_${PER}_fit_${FIT}_*.csv
#                             let "c+=1"
#                             echo "ploting $c"
#                             # male sigma
#                             python /Users/andrea/Documents/GitHub/Female-Choosing-Project/plot.py -inf CSVResultFiles/July8/ml_${ML}_ms_*_fsigma_${FSIGMA}_fmu_${FM}_me_${ME}_selper_${PER}_fit_${FIT}_*.csv -outfolder male_sigma -out ml_${ML}_fsigma_${FSIGMA}_fmu_${FM}_me_${ME}_selper_${PER}_fit_${FIT} -ing CSVResultFiles/July8/geno_ml_${ML}_ms_*_fsigma_${FSIGMA}_fmu_${FM}_me_${ME}_selper_${PER}_fit_${FIT}_*.csv
#                             let "c+=1"
#                             echo "ploting $c"
#                             # female mu
#                             python /Users/andrea/Documents/GitHub/Female-Choosing-Project/plot.py -inf CSVResultFiles/July8/ml_${ML}_ms_${MS}_fsigma_${FSIGMA}_fmu_*_me_${ME}_selper_${PER}_fit_${FIT}_*.csv -outfolder female_mu -out ml_${ML}_ms_${MS}_fsigma_${FSIGMA}_me_${ME}_selper_${PER}_fit_${FIT} -ing CSVResultFiles/July8/geno_ml_${ML}_ms_*_fsigma_${FSIGMA}_fmu_${FM}_me_${ME}_selper_${PER}_fit_${FIT}_*.csv
#                             let "c+=1"
#                             echo "ploting $c"
#                         done
#                     done
#                 done
#             done
#         done
#     done
# done


# --------------------------------------Smaller trails--------------------------------------------

# for MS in 5
# do
#     for MU in 0.001
#     do
#         for FIT in 1 0
#         do           
#             # 10 trails for each set of parameters
#             for V in {1..10}
#             do
#                 python /Users/andrea/Documents/GitHub/Female-Choosing-Project/run.py -ml 20 -ms ${MS} -fsigma 1 -fmu 5 -fit ${FIT} -fn "ms_${MS}_fit_${FIT}_cost_1_mut_${MU}_$V" -ft 1 -memol 20 -c 1 -d ${date} -mul ${MU} -max 500
#                 # pids[${count}]=$!
#                 let "count+=1"
#                 echo "running $count"
#             done
#         done
#     done
# done


for MS in 5
do
    for MU in 0.001 0.003 0.005
    do
        # male sigma
        let "c+=1"
        echo "ploting $c"        
        python /Users/andrea/Documents/GitHub/Female-Choosing-Project/plot.py -inf CSVResultFiles/$date/ms_${MS}_fit_*_cost_1_mut_${MU}_*.csv -outfolder ${date}/fitness_function -out ms_${MS}_cost_1_mut_${MU} -ing CSVResultFiles/$date/last_ms_${MS}_fit_*_cost_1_mut_${MU}_*.csv
        echo "finished ploting $c"
    done
done