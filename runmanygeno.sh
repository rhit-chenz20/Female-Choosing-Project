# #!/bin/bash
# count = 0
# # maleMu = 5
# # 4 different mating length, aka how many chances a female gets for mating
# for ML in 5 10 20
# do
#     # 3 different male sigma
#     for MS in 1 10 100
#     do
#         # 3 female memory
#         for ME in 0 5 10
#         do
#             #10 trails for each set of parameters
#             for V in {1..10}
#             do
#                 python /Users/andrea/Documents/GitHub/Female-Choosing-Project/run.py -ml $ML -ms $MS -fsigma 2 -fmu 5 -fn "ml_${ML}_ms_${MS}_me_${ME}_$V" -ft 1 -memol ${ME}
#                 # pids[${count}]=$!
#                 let "count+=1"
#                 echo "running $count"
#             done
#         done
#     done
# done

# for pid in ${pids[*]}
# do
#     wait $pid
# done

c=0
# 4 different mating length, aka how many chances a female gets for mating
for ML in 5 10 20
do
    # 3 different male sigma
    for MS in 1 10 100
    do
        # 3 female memory
        for ME in 0 5 10
        do
            python /Users/andrea/Documents/GitHub/Female-Choosing-Project/plot.py -inf CSVResultFiles/June29/ml_${ML}_ms_${MS}_me_${ME}_*.csv -out ml_${ML}_ms_${MS}_me_${ME} -ing CSVResultFiles/June29/geno_ml_${ML}_ms_${MS}_me_${ME}_*.csv
            let "c+=1"
            echo "plotting $c"
        done
    done
done

echo "finished"

#  -----------------------------------test trial----------------------------

# 3 female memory
# count = 1
# for ME in 0 5 10
# do
#     #10 trails for each set of parameters
#     for V in {1..10}
#     do
#         python /Users/andrea/Documents/GitHub/Female-Choosing-Project/run.py -ml 10 -ms 3 -fsigma 2 -fmu 5 -fn "me_${ME}_$V" -ft 1 -memol ${ME}
#         # pids[${count}]=$!
#         echo "running $count"
#         let "count+=1"
#     done
# done
# 3 female memory
# c=1
# for ME in 0 5 10
# do
#     python /Users/andrea/Documents/GitHub/Female-Choosing-Project/plot.py -inf CSVResultFiles/June29/me_${ME}_*.csv -out me_${ME} -ing CSVResultFiles/June29/geno_me_${ME}_*.csv
#     echo "plotting $c"
#     let "c+=1"
# done
