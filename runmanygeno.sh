#!/bin/bash
declare date="Aug17"
mkdir "../result"
mkdir "../result/${date}"
mkdir "../result/${date}/CSV"
mkdir "../result/${date}/plot"
mkdir "../result/${date}/CSV/Learning"
mkdir "../result/${date}/plot/Learning"

declare c=0
declare count=0
declare max=30

# for MS in 1
# do
#     for FS in 10
#     do
#         for FM in 1
#         do
#             for COST in 0
#             do
#                 for FIT in 0
#                 do
#                     for ML in 3 5
#                     do
#                         for V in {1..5}
#                         do
#                             let "count+=1"
#                             echo "running $count"

#                             python3 run.py -ml $ML -ms $MS -fsigma $FS -fmu $FM -fit $FIT -fn "../result/${date}/CSV/Learning/ml_${ML}_ms_${MS}_fit_${FIT}_cost_${COST}_$V" -ft 1 -sel 0 -c $COST -max 500
#                             # if ((count>$max))
#                             # then
#                             #     wait
#                             #     let "count=0"
#                             # fi
#                         done
#                     done
#                 done
#             done
#         done
#     done
# done              
# echo "finished simulation. now plotting"

# bash plotgeno.sh

for MS in 10
do
    for FS in 10
    do
        for FM in 1
        do
            for COST in 0
            do
                for FIT in 0
                do
                    for ML in 3 5
                    do
                        for V in {1..100}
                        do
                            let "count+=1"
                            echo "running $count"

                            python3 run.py -ml $ML -ms $MS -fsigma $FS -fmu $FM -fit $FIT -fn "../result/${date}/CSV/Learning/ml_${ML}_ms_${MS}_fit_${FIT}_cost_${COST}_$V" -ft 1 -sel 0 -c $COST -max 5000 -memol $ML &
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

bash plotgeno.sh