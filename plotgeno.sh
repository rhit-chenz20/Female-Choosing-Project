declare date="Aug14"
declare c=0
declare max=30

mkdir ../result/${date}/plot/Learning/mating_length
mkdir ../result/${date}/plot/Learning/male_sigma
mkdir ../result/${date}/plot/Learning/fitness_function
mkdir ../result/${date}/plot/Learning/cost
mkdir ../result/${date}/plot/Learning/memory

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
#                     # ploting mating length

#                     let "c+=1"
#                     python3 plot.py -inf ../result/${date}/CSV/Learning/ml_*_ms_${MS}_fit_${FIT}_cost_${COST}_*.csv -out ../result/${date}/plot/Learning/mating_length/ms_${MS}_fit_${FIT}_cost_${COST} -t 1 -ing ../result/${date}/CSV/Learning/last_ml_*_ms_${MS}_fit_${FIT}_cost_${COST}_*.csv
#                     echo "finished plotting $c"
                    
#                     if ((c>$max))
#                         then
#                             wait
#                             let "c=0"
#                         fi
#                 done
#             done
#         done
#     done            
# done
                    
# echo "finished plotting"

for MS in 1 5 10
do
    for FS in 10
    do
        for FM in 1
        do
            for COST in 0 1 3
            do
                for FIT in 0 1 2
                do
                    for ML in 3 5 10 20
                    do
                        for MR in 0 1 3 5 10 20
                        do
                        # ploting mating length

                        let "c+=1"
                        python3 plot.py -inf ../result/${date}/CSV/Learning/ml_${ML}_ms_${MS}_fit_${FIT}_cost_${COST}_memory_*_*.csv -out ../result/${date}/plot/Learning/memory/ml_${ML}ms_${MS}_fit_${FIT}_cost_${COST} -t 1 -ing ../result/${date}/CSV/Learning/last_ml_${ML}_ms_${MS}_fit_${FIT}_cost_${COST}_memory_*_*.csv &
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
done
                    
echo "finished plotting"

bash runmany.sh