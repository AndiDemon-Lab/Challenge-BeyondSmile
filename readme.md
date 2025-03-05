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

### Accuracy (Drop NaN)
<table>
  <thead>
    <tr>
      <th>Algorithm</th>
      <th>Full Features (Drop NaN)</th>
      <th>Eyes and Smile Probability (Drop NaN)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>AdaBoost</td>
      <td>0.6112</td>
      <td>0.4334</td>
    </tr>
    <tr>
      <td>Bagging</td>
      <td>0.5130</td>
      <td>0.6649</td>
    </tr>
    <tr>
      <td>CatBoost</td>
      <td>0.5785</td>
      <td>0.7058</td>
    </tr>
    <tr>
      <td>GradientBoosting</td>
      <td>0.5841</td>
      <td>0.5415</td>
    </tr>
    <tr>
      <td>LightGBM</td>
      <td>0.5788</td>
      <td>0.6726</td>
    </tr>
    <tr>
      <td>RandomForest</td>
      <td>0.5037</td>
      <td>0.6607</td>
    </tr>
    <tr>
      <td>XGBoost</td>
      <td>0.5774</td>
      <td>0.5649</td>
    </tr>
    <tr>
      <td>LSTM</td>
      <td>0.5534</td>
      <td>0.6563</td>
    </tr>
  </tbody>
</table>

### Accuracy (Imputed Mean)
<table>
  <thead>
    <tr>
      <th>Algorithm</th>
      <th>Full Features (Imputed Mean)</th>
      <th>Eyes and Smile Probability (Imputed Mean)</th>
      <th>Head Euler Angle</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>AdaBoost</td>
      <td>0.6112</td>
      <td>0.4255</td>
      <td>0.4708</td>
    </tr>
    <tr>
      <td>Bagging</td>
      <td>0.5130</td>
      <td>0.6564</td>
      <td>0.5451</td>
    </tr>
    <tr>
      <td>CatBoost</td>
      <td>0.5785</td>
      <td>0.6978</td>
      <td>0.4366</td>
    </tr>
    <tr>
      <td>GradientBoosting</td>
      <td>0.5841</td>
      <td>0.5343</td>
      <td>0.4324</td>
    </tr>
    <tr>
      <td>LightGBM</td>
      <td>0.5788</td>
      <td>0.6663</td>
      <td>0.4367</td>
    </tr>
    <tr>
      <td>RandomForest</td>
      <td>0.5037</td>
      <td>0.6498</td>
      <td>0.5113</td>
    </tr>
    <tr>
      <td>XGBoost</td>
      <td>0.5774</td>
      <td>0.5564</td>
      <td>0.4417</td>
    </tr>
    <tr>
      <td>LSTM</td>
      <td>0.5269</td>
      <td>0.6430</td>
      <td>0.5193</td>
    </tr>
  </tbody>
</table>


## Hybrid Model


