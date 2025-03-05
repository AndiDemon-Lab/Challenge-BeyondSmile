# BeyondSmile

## Description
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

## Methods
In this project, we evaluated the performance of various machine learning algorithms on data with missing values. The following algorithms were applied:
- **AdaBoost**
- **Bagging**
- **CatBoost**
- **GradientBoosting**
- **LightGBM**
- **RandomForest**
- **XGBoost**
- **LSTM**

Two strategies were employed to handle missing data:
1. **Drop NaN:** Rows with missing values were removed.
2. **Imputed Mean:** Missing values were replaced with the mean value of the corresponding feature.


## Results

## Universal Model
This universal model employ Leave One Participant Out Cross validation to make generelized model

<table>
    <caption>F1 Scores for Different Models and Feature Sets Drop NaN</caption>
    <tr>
        <th>Algorithm</th>
        <th>Full Features (Drop NaN)</th>
        <th>Eyes and Smile Probability (Drop NaN)</th>
    </tr>
    <tr><td>AdaBoost</td><td>0.3994</td><td>0.4073</td></tr>
    <tr><td>Bagging</td><td>0.3278</td><td>0.7093</td></tr>
    <tr><td>CatBoost</td><td>0.3812</td><td>0.7388</td></tr>
    <tr><td>GradientBoosting</td><td>0.3914</td><td>0.5704</td></tr>
    <tr><td>LightGBM</td><td>0.3806</td><td>0.7096</td></tr>
    <tr><td>RandomForest</td><td>0.3351</td><td>0.7046</td></tr>
    <tr><td>XGBoost</td><td>0.3800</td><td>0.5920</td></tr>
    <tr><td>LSTM</td><td>0.0688</td><td>0.0484</td></tr>
</table>

<table>
    <caption>F1-Score Performance of Different Models with Imputed Mean Features</caption>
    <tr>
        <th>Algorithm</th>
        <th>Full Features (Imputed Mean)</th>
        <th>Eyes and Smile Probability (Imputed Mean)</th>
        <th>Head Euler Angle</th>
    </tr>
    <tr><td>AdaBoost</td><td>0.3994</td><td>0.3885</td><td>0.2013</td></tr>
    <tr><td>Bagging</td><td>0.3278</td><td>0.6995</td><td>0.1593</td></tr>
    <tr><td>CatBoost</td><td>0.3812</td><td>0.7289</td><td>0.1835</td></tr>
    <tr><td>GradientBoosting</td><td>0.3914</td><td>0.5613</td><td>0.1905</td></tr>
    <tr><td>LightGBM</td><td>0.3806</td><td>0.7024</td><td>0.1853</td></tr>
    <tr><td>RandomForest</td><td>0.3351</td><td>0.6922</td><td>0.1700</td></tr>
    <tr><td>XGBoost</td><td>0.3800</td><td>0.5806</td><td>0.1847</td></tr>
    <tr><td>LSTM</td><td>0.1337</td><td>0.0227</td><td>0.0810</td></tr>
</table>

<table>
    <caption>AUROC Scores for Different Models and Feature Sets (Drop NaN)</caption>
    <tr>
        <th>Algorithm</th>
        <th>Full Features (Drop NaN)</th>
        <th>Eyes and Smile Probability (Drop NaN)</th>
    </tr>
    <tr><td>AdaBoost</td><td>0.5485</td><td>0.5156</td></tr>
    <tr><td>Bagging</td><td>0.5061</td><td>0.7476</td></tr>
    <tr><td>CatBoost</td><td>0.5492</td><td>0.7845</td></tr>
    <tr><td>GradientBoosting</td><td>0.5511</td><td>0.6173</td></tr>
    <tr><td>LightGBM</td><td>0.5487</td><td>0.7525</td></tr>
    <tr><td>RandomForest</td><td>0.5083</td><td>0.7432</td></tr>
    <tr><td>XGBoost</td><td>0.5490</td><td>0.6538</td></tr>
    <tr><td>LSTM</td><td>0.2493</td><td>0.2202</td></tr>
</table>

<table>
    <caption>AUROC Scores for Different Models with Imputed Mean Features</caption>
    <tr>
        <th>Algorithm</th>
        <th>Full Features (Imputed Mean)</th>
        <th>Eyes and Smile Probability (Imputed Mean)</th>
        <th>Head Euler Angle</th>
    </tr>
    <tr><td>AdaBoost</td><td>0.5485</td><td>0.5001</td><td>0.4079</td></tr>
    <tr><td>Bagging</td><td>0.5061</td><td>0.7396</td><td>0.5996</td></tr>
    <tr><td>CatBoost</td><td>0.5492</td><td>0.7774</td><td>0.4676</td></tr>
    <tr><td>GradientBoosting</td><td>0.5511</td><td>0.6033</td><td>0.4393</td></tr>
    <tr><td>LightGBM</td><td>0.5487</td><td>0.7431</td><td>0.4450</td></tr>
    <tr><td>RandomForest</td><td>0.5083</td><td>0.7307</td><td>0.5922</td></tr>
    <tr><td>XGBoost</td><td>0.5490</td><td>0.6347</td><td>0.4748</td></tr>
    <tr><td>LSTM</td><td>0.3379</td><td>0.2414</td><td>0.2938</td></tr>
</table>

<table>
    <caption>Accuracy Scores for Different Models and Feature Sets (Drop NaN)</caption>
    <tr>
        <th>Algorithm</th>
        <th>Full Features (Drop NaN)</th>
        <th>Eyes and Smile Probability (Drop NaN)</th>
    </tr>
    <tr><td>AdaBoost</td><td>0.6112</td><td>0.4334</td></tr>
    <tr><td>Bagging</td><td>0.5130</td><td>0.6649</td></tr>
    <tr><td>CatBoost</td><td>0.5785</td><td>0.7058</td></tr>
    <tr><td>GradientBoosting</td><td>0.5841</td><td>0.5415</td></tr>
    <tr><td>LightGBM</td><td>0.5788</td><td>0.6726</td></tr>
    <tr><td>RandomForest</td><td>0.5037</td><td>0.6607</td></tr>
    <tr><td>XGBoost</td><td>0.5774</td><td>0.5649</td></tr>
    <tr><td>LSTM</td><td>0.5534</td><td>0.6563</td></tr>
</table>

<table>
    <caption>Accuracy Scores for Different Models with Imputed Mean Features</caption>
    <tr>
        <th>Algorithm</th>
        <th>Full Features (Imputed Mean)</th>
        <th>Eyes and Smile Probability (Imputed Mean)</th>
        <th>Head Euler Angle</th>
    </tr>
    <tr><td>AdaBoost</td><td>0.6112</td><td>0.4255</td><td>0.4708</td></tr>
    <tr><td>Bagging</td><td>0.5130</td><td>0.6564</td><td>0.5451</td></tr>
    <tr><td>CatBoost</td><td>0.5785</td><td>0.6978</td><td>0.4366</td></tr>
    <tr><td>GradientBoosting</td><td>0.5841</td><td>0.5343</td><td>0.4324</td></tr>
    <tr><td>LightGBM</td><td>0.5788</td><td>0.6663</td><td>0.4367</td></tr>
    <tr><td>RandomForest</td><td>0.5037</td><td>0.6498</td><td>0.5113</td></tr>
    <tr><td>XGBoost</td><td>0.5774</td><td>0.5564</td><td>0.4417</td></tr>
    <tr><td>LSTM</td><td>0.5269</td><td>0.6430</td><td>0.5193</td></tr>
</table>



## Hybrid Model



<table>
    <caption>AUROC Comparison of different algorithms using Full Features (Drop NaN) and Eyes and Smile Probability (Drop NaN).</caption>
    <thead>
        <tr>
            <th>Algorithm</th>
            <th>Full Features (Drop NaN)</th>
            <th>Eyes and Smile Probability (Drop NaN)</th>
        </tr>
    </thead>
    <tbody>
        <tr><td>AdaBoost</td><td>0.5302</td><td>0.4622</td></tr>
        <tr><td>Bagging</td><td>0.5107</td><td>0.5007</td></tr>
        <tr><td>CatBoost</td><td>0.4967</td><td>0.5039</td></tr>
        <tr><td>GradientBoosting</td><td>0.5188</td><td>0.4786</td></tr>
        <tr><td>LightGBM</td><td>0.4999</td><td>0.4971</td></tr>
        <tr><td>RandomForest</td><td>0.5012</td><td>0.4995</td></tr>
        <tr><td>XGBoost</td><td>0.5061</td><td>0.4987</td></tr>
        <tr><td>LSTM</td><td>0.4559</td><td>0.4487</td></tr>
    </tbody>
</table>

<table>
    <caption>AUROC Comparison of different algorithms using Full Features (Imputed Mean), Eyes and Smile Probability (Imputed Mean), and Head Euler Angle.</caption>
    <thead>
        <tr>
            <th>Algorithm</th>
            <th>Full Features (Imputed Mean)</th>
            <th>Eyes and Smile Probability (Imputed Mean)</th>
            <th>Head Euler Angle</th>
        </tr>
    </thead>
    <tbody>
        <tr><td>AdaBoost</td><td>0.5093</td><td>0.4663</td><td>0.5296</td></tr>
        <tr><td>Bagging</td><td>0.5240</td><td>0.4950</td><td>0.5144</td></tr>
        <tr><td>CatBoost</td><td>0.5074</td><td>0.4942</td><td>0.5232</td></tr>
        <tr><td>GradientBoosting</td><td>0.5054</td><td>0.4729</td><td>0.5275</td></tr>
        <tr><td>LightGBM</td><td>0.5204</td><td>0.4910</td><td>0.5273</td></tr>
        <tr><td>RandomForest</td><td>0.5249</td><td>0.4921</td><td>0.5153</td></tr>
        <tr><td>XGBoost</td><td>0.5140</td><td>0.4889</td><td>0.5240</td></tr>
        <tr><td>LSTM</td><td>0.5201</td><td>0.4490</td><td>0.4506</td></tr>
    </tbody>
</table>

<table>
    <caption>Accuracy Comparison of different algorithms using Full Features (Drop NaN) and Eyes and Smile Probability (Drop NaN).</caption>
    <thead>
        <tr>
            <th>Algorithm</th>
            <th>Full Features (Drop NaN)</th>
            <th>Eyes and Smile Probability (Drop NaN)</th>
        </tr>
    </thead>
    <tbody>
        <tr><td>AdaBoost</td><td>0.3994</td><td>0.4073</td></tr>
        <tr><td>Bagging</td><td>0.3278</td><td>0.7093</td></tr>
        <tr><td>CatBoost</td><td>0.3812</td><td>0.7388</td></tr>
        <tr><td>GradientBoosting</td><td>0.3914</td><td>0.5704</td></tr>
        <tr><td>LightGBM</td><td>0.3806</td><td>0.7096</td></tr>
        <tr><td>RandomForest</td><td>0.3351</td><td>0.7046</td></tr>
        <tr><td>XGBoost</td><td>0.3800</td><td>0.5920</td></tr>
        <tr><td>LSTM</td><td>0.0688</td><td>0.0484</td></tr>
    </tbody>
</table>

<table>
    <caption>Accuracy Comparison of different algorithms using Full Features (Imputed Mean), Eyes and Smile Probability (Imputed Mean), and Head Euler Angle.</caption>
    <thead>
        <tr>
            <th>Algorithm</th>
            <th>Full Features (Imputed Mean)</th>
            <th>Eyes and Smile Probability (Imputed Mean)</th>
            <th>Head Euler Angle</th>
        </tr>
    </thead>
    <tbody>
        <tr><td>AdaBoost</td><td>0.3994</td><td>0.3885</td><td>0.2013</td></tr>
        <tr><td>Bagging</td><td>0.3278</td><td>0.6995</td><td>0.1593</td></tr>
        <tr><td>CatBoost</td><td>0.3812</td><td>0.7289</td><td>0.1835</td></tr>
        <tr><td>GradientBoosting</td><td>0.3914</td><td>0.5613</td><td>0.1905</td></tr>
        <tr><td>LightGBM</td><td>0.3806</td><td>0.7024</td><td>0.1853</td></tr>
        <tr><td>RandomForest</td><td>0.3351</td><td>0.6922</td><td>0.1700</td></tr>
        <tr><td>XGBoost</td><td>0.3800</td><td>0.5806</td><td>0.1847</td></tr>
        <tr><td>LSTM</td><td>0.1337</td><td>0.0227</td><td>0.0810</td></tr>
    </tbody>
</table>

<table>
    <caption>F1-Score Comparison of Different Algorithms Using Full Features (Drop NaN) and Eyes and Smile Probability (Drop NaN)</caption>
    <thead>
        <tr>
            <th>Algorithm</th>
            <th>Full Features (Drop NaN)</th>
            <th>Eyes and Smile Probability (Drop NaN)</th>
        </tr>
    </thead>
    <tbody>
        <tr><td>AdaBoost</td><td>0.4215</td><td>0.3577</td></tr>
        <tr><td>Bagging</td><td>0.3495</td><td>0.2931</td></tr>
        <tr><td>CatBoost</td><td>0.4072</td><td>0.1647</td></tr>
        <tr><td>GradientBoosting</td><td>0.4085</td><td>0.3554</td></tr>
        <tr><td>LightGBM</td><td>0.3965</td><td>0.2464</td></tr>
        <tr><td>RandomForest</td><td>0.3445</td><td>0.2946</td></tr>
        <tr><td>XGBoost</td><td>0.4125</td><td>0.3391</td></tr>
        <tr><td>LSTM</td><td>0.3713</td><td>0.4099</td></tr>
    </tbody>
</table>

