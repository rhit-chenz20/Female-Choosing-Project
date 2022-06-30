#!/bin/bash
# conda activate female-mating
count = 0
# maleMu = 5
# 4 different mating length, aka how many chances a female gets for mating
for ML in 1 5 10
do
    # 3 different male sigma
    for MS in 1 10 100
    do
        # 3 female figma
        for SR in 0.01 1 10
        do
            #10 trails for each set of parameters
            for V in {1..10}
            do
                python /Users/andrea/Documents/GitHub/Female-Choosing-Project/run.py -ml $ML -ms $MS -mus 0.1 -fsigma $SR -fmu 5 -fit 1 -fn "ml_${ML}_ms_${MS}_mus_${MuS}_fsigma_${SR}_$V"
                # pids[${count}]=$!
                echo "running $count"
                let "count+=1"
            done
        done
    done
done

# for pid in ${pids[*]}
# do
#     wait $pid
# done

c=1
# 4 different mating length, aka how many chances a female gets for mating
for ML in 1 5 10
do
    # 3 different male sigma
    for MS in 1 10 100
    do
        # 3 female figma
        for SR in 0.01 1 10
        do
            python /Users/andrea/Documents/GitHub/Female-Choosing-Project/plot.py -in CSVResultFiles/June28/ml_${ML}_ms_${MS}_mus__fsigma_${SR}_*.csv -out ml_${ML}_ms_${MS}_mus__fsigma_${SR}
            echo "plotting $c"
            let "c+=1"
           
        done
    done
done

echo "finished"