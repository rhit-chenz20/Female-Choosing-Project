# # !/bin/bash
# count = 0
# # maleMu = 5
# # 3 female mu
# for FM in -5 5 15
# do
#     # 3 different male sigma
#     for MS in 1 10 100
#     do
#         for FSIGMA in 1 10 100
#         do
#             # 3 female memory
#             for ME in 0 5 10
#             do
#                 #10 trails for each set of parameters
#                 for V in {1..10}
#                 do
#                     python /Users/andrea/Documents/GitHub/Female-Choosing-Project/run.py -ml 20 -ms $MS -fsigma $FSIGMA -fmu $FM -fit 1 -fn "ms_${MS}_fsigma_${FSIGMA}_fmu_${FM}_me_${ME}_$V" -ft 1 -memol ${ME}
#                     # pids[${count}]=$!
#                     let "count+=1"
#                     echo "running $count"
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

# python /Users/andrea/Documents/GitHub/Female-Choosing-Project/plot.py -inf CSVResultFiles/July6/ms_1_fsigma_1_fmu_*_me_0_*.csv -out ms_1_fsigma_1_fmu_${FM}_me_${ME} -ing CSVResultFiles/July6/geno_ms_${MS}_fsigma_${MS}_fmu_${FM}_me_${ME}_*.csv




# 4 different mating length, aka how many chances a female gets for mating
# for FM in -5 5 15
# do
#     # 3 different male sigma
#     for MS in 1 10 100
#     do
#         # 3 female memory
#         for ME in 0 5 10
#         do
#             python /Users/andrea/Documents/GitHub/Female-Choosing-Project/plot.py -inf CSVResultFiles/July6/ms_${MS}_fsigma_${MS}_fmu_${FM}_me_${ME}_*.csv -out ms_${MS}_fsigma_${MS}_fmu_${FM}_me_${ME} -ing CSVResultFiles/July6/geno_ms_${MS}_fsigma_${MS}_fmu_${FM}_me_${ME}_*.csv
#             let "c+=1"
#             echo "plotting $c"
#         done
#     done
# done

# echo "finished"

#  -----------------------------------test trial----------------------------

# 3 female memory
# count = 1
# for ME in 0
# do
#     for MS in 1 5
#     do
#         for FSIGMA in 1 5
#         do
#             #10 trails for each set of parameters
#             for V in {1..10}
#             do
#                 python /Users/andrea/Documents/GitHub/Female-Choosing-Project/run.py -ml 10 -ms $MS -fsigma $FSIGMA -fmu 5 -fn "me_${ME}_ms_${MS}_fsigma_${FSIGMA}_${V}_" -ft 1 -memol ${ME}
#                 # pids[${count}]=$!
#                 echo "running $count"
#                 let "count+=1"
#             done
#         done
#     done
# done

# c=1
# for MS in 1 5
# do
#     python /Users/andrea/Documents/GitHub/Female-Choosing-Project/plot.py -inf CSVResultFiles/July6/me_0_ms_${MS}_fsigma_1_*.csv -out me_0_ms_${MS}_fsigma_1 -ing CSVResultFiles/July6/geno_me_0_ms_${MS}_fsigma_1_*.csv 
#     echo "ploting $c"
#     let "c+=1"
# done

python /Users/andrea/Documents/GitHub/Female-Choosing-Project/plot.py -inf CSVResultFiles/July6/me_0_ms_1_fsigma_1_*.csv CSVResultFiles/July6/me_0_ms_5_fsigma_1_*.csv -out me_0_ms_1_fsigma_1 -ing CSVResultFiles/July6/geno_me_0_ms_*_fsigma_1_*.csv