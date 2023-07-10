#!/bin/bash
declare date="June11"
mkdir "result"
mkdir "result/${date}"
mkdir "result/${date}/CSV"
mkdir "result/${date}/Fig"

declare c=0
declare count=0
declare max=10
declare V=1
declare T=0.5

mkdir "result/${date}/Fig/top_${T}"

# learning model
for MS in 10
do
    for FIT in 2
    do
        for ML in 10
        do
            for SZ in 500
            do
                for FITBASE in 1
                do
                    let "count+=1"
                    echo "running $count"

                    python3 run.py -fs $SZ -ml $ML -ms $MS -fit $FIT -fitbase $FITBASE -fn "result/${date}/CSV/ml_${ML}_ms_${MS}_fit_${FIT}_fitbase_${FITBASE}_${V}" &
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
# echo "finished simulation"

# for MS in 1 5 10
# do
#     for FIT in 2
#     do
#         for ML in 3
#         do
#             for SZ in 100
#             do
#                 let "count+=1"
#                 echo "running $count"

#                 python3 bar_plot.py -c Ave_fit -fn result/${date}/CSV/ml_*_ms_${MS}_fit_${FIT}_${V}_models.csv -o result/${date}/Fig/top_${T}/ms_${MS}_fit_${FIT}_t_${T}_sort_fit.png -t $T &
#                 python3 bar_plot.py -c Sum_fit -fn result/${date}/CSV/ml_*_ms_${MS}_fit_${FIT}_${V}_models.csv -o result/${date}/Fig/top_${T}/ms_${MS}_fit_${FIT}_t_${T}_sort_sumfit.png -t $T &
#                 if ((count>$max))
#                 then
#                     wait
#                     let "count=0"
#                 fi
#             done
#         done
#     done
# done          
