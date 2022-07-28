#!/bin/bash
declare date="July26"
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
#         python /Users/andrea/Documents/GitHub/Female-Choosing-Project/run.py -ml 10 -ms 3 -fsigma 3 -fmu 5 -fit 0 -fn "thre_sel_${SEL}_$V" -ft 0 -sel $SEL -d ${date}
#     done
# done

# let "c+=1"
# echo "plotting $c"
# python /Users/andrea/Documents/GitHub/Female-Choosing-Project/plot.py -inf CSVResultFiles/${date}/thre_sel${SEL}_*.csv -outfolder ${date}/threshold/selection -out selection -t 0
# echo "finished $c"



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
                        for V in {1..10}
                        do
                            let "c+=1"
                            echo "running $c"
                            python /Users/andrea/Documents/GitHub/Female-Choosing-Project/run.py -ml 20 -ms $MS -fsigma $FS -fmu $FM -fit $FIT -fn "sel_${SEL}_ms_${MS}_fs_${FS}_fmu_${FM}_fit_${FIT}_cost_${COST}_$V" -ft 0 -sel $SEL -d ${date} -c $COST
                        done
                    done
                done
            done
        done
    done              
done

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
#                     let "c+=1"
#                     echo "plotting $c"
#                     python /Users/andrea/Documents/GitHub/Female-Choosing-Project/plot.py -inf CSVResultFiles/${date}/thre_sel${SEL}_*.csv -outfolder ${date}/threshold/selection -out selection -t 0
#                     echo "finished $c"
#                     done
#                 done
#             done
#         done
#     done            
# done
