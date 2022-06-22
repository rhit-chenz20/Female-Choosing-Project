#!/bin/bash
conda activate female-mating
count = 0
# maleMu = 5
# 4 different mating length, aka how many chances a female gets for mating
# for ML in 1 5 10 20
# do
#     # 3 different male sigma
#     for MS in 1 10 100
#     do
#         # 3 different mutation sigma
#         for MuS in 0.1 0.001 0.00001
#         do
#             # 3 starting range
#             for SR in 0.01 1 10
#             do
#                 #10 trails for each set of parameters
#                 for V in {1..10}
#                 do
#                     python /Users/andrea/Documents/GitHub/Female-Choosing-Project/run.py 20 $ML 5 $MS $MuS 500 $SR 0 0 "ml_${ML}_ms_${MS}_mus_${MuS}_sr_${SR}_$V"
#                     pids[${count}]=$!
#                     echo "running $count"
#                     let "count+=1"
#                 done
#             done
#         done
#     done
# done

# for pid in ${pids[*]}
# do
#     wait $pid
# done

c=0
for ML in 1 5 10 20
do
    # 3 different male sigma
    for MS in 1 10 100
    do
        # 3 different mutation sigma
        for MuS in 0.1 0.001 0.00001
        do
            # 3 starting range
            for SR in 0.01 1 10
            do
                python /Users/andrea/Documents/GitHub/Female-Choosing-Project/plot.py "ml_${ML}_ms_${MS}_mus_${MuS}_sr_${SR}"
                echo "ploting $c"
                let "c+=1"
            done
        done
    done
done

#echo python /Users/andrea/Documents/GitHub/Female-Choosing-Project/plot.py "test_mm1_mr3_s_t_*" &

echo "finished"