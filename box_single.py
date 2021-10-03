import pandas as pd
import matplotlib.pyplot as plt


file_path = r'G:\Lobectomy\shengjing\RLL_nii\RL.xls'

percent = pd.read_excel(io=file_path, sheet_name=3, header=None)


value = percent.values[:, 1:]

percent_Data = pd.DataFrame(value)

plt.boxplot(percent_Data,  labels=['RU', 'RM', 'RL', 'LU',  'LL'], patch_artist=True)
plt.ylim(-0.5, 2)
plt.savefig('RLL_percent_shengjing.png')  # 保存图片
plt.show()
