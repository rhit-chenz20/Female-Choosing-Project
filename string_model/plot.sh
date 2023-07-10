#!/bin/bash
declare date="June11"
mkdir "result"
mkdir "result/${date}"
mkdir "result/${date}/CSV"
mkdir "result/${date}/CSV/processed"
mkdir "result/${date}/Fig"

declare bv=1.0
declare sv=1.0

# for FB in 0.25 0.5 0.75 1.0
# do
#     python bar_plot.py -fn result/June11/CSV/processed/lowest_base_fb_${FB}_b*e_1.0_s*e_1.0.csv -o result/June11/Fig/fb_0.25.png -c 1
# done

# for BE in 0 1
# do
#     for SE in 0 1
#     do
#         # lowest male as base
#         python filterdata.py -nf base.csv -fn result/${date}/CSV/* -bv 1 -be $BE -se $SE -sv 1 -o result/${date}/CSV/processed/lowest_base
        
#         if [[ $BE -eq 0 ]]
#         then
#             if [[ $SE -eq 0 ]]
#             then
#                 python bar_plot.py -fn result/${date}/CSV/processed/lowest_base_fb_*_ble_${bv}_sle_${sv}.csv -o result/${date}/Fig/lowest_base_ble_${bv}_sle_${sv}.png
#             elif [[ $SE -eq 1 ]]
#             then
#                 python bar_plot.py -fn result/${date}/CSV/processed/lowest_base_fb_*_ble_${bv}_sge_${sv}.csv -o result/${date}/Fig/lowest_base_ble_${bv}_sge_${sv}.png
#             fi
#         elif [[ $BE -eq 1 ]]
#         then
#             if [[ $SE -eq 0 ]]
#             then
#                 python bar_plot.py -fn result/${date}/CSV/processed/lowest_base_fb_*_bge_${bv}_sle_${sv}.csv -o result/${date}/Fig/lowest_base_bge_${bv}_sle_${sv}.png
#             elif [[ $SE -eq 1 ]]
#             then
#                 python bar_plot.py -fn result/${date}/CSV/processed/lowest_base_fb_*_bge_${bv}_sge_${sv}.csv -o result/${date}/Fig/lowest_base_bge_${bv}_sge_${sv}.png
#             fi
#         fi


#         # average male as base
#         python filterdata.py -nf base_ave.csv -fn result/${date}/CSV/* -bv 1 -be $BE -se $SE -sv 1 -o result/${date}/CSV/processed/ave_base
#         if [[ $BE -eq 0 ]]
#         then
#             if [[ $SE -eq 0 ]]
#             then
#                 python bar_plot.py -fn result/${date}/CSV/processed/ave_base_fb_*_ble_${bv}_sle_${sv}.csv -o result/${date}/Fig/ave_base_ble_${bv}_sle_${sv}.png
#             elif [[ $SE -eq 1 ]]
#             then
#                 python bar_plot.py -fn result/${date}/CSV/processed/ave_base_fb_*_ble_${bv}_sge_${sv}.csv -o result/${date}/Fig/ave_base_ble_${bv}_sge_${sv}.png
#             fi
#         elif [[ $BE -eq 1 ]]
#         then
#             if [[ $SE -eq 0 ]]
#             then
#                 python bar_plot.py -fn result/${date}/CSV/processed/ave_base_fb_*_bge_${bv}_sle_${sv}.csv -o result/${date}/Fig/ave_base_bge_${bv}_sle_${sv}.png
#             elif [[ $SE -eq 1 ]]
#             then
#                 python bar_plot.py -fn result/${date}/CSV/processed/ave_base_fb_*_bge_${bv}_sge_${sv}.csv -o result/${date}/Fig/ave_base_bge_${bv}_sge_${sv}.png
#             fi
#         fi

#     done
# done