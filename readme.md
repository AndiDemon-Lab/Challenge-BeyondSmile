# BeyondSmile

## Description
Depression is a significant global health burden, affecting over 322 mil-
lion people worldwide and projected to surpass cardiovascular disease as
the leading cause of disability by 2030. Despite advancements in mental
health services, accurate and accessible diagnostic methods remain a crit-
ical challenge. Traditional approaches, such as psychiatric consultations,
face limitations due to the physician-patient ratio and reliance on subjec-
tive self-report scales, which can lead to inaccuracies. Recent research has
explored alternative methods, including facial behavior analysis, for objec-
tive depression assessment. This approach is cost-effective, non-invasive,
and suitable for real-world applications. This study builds upon existing
research, such as FacePsy and MoodCapture, by enhancing facial behavior
analysis using deep learning techniques. We propose an improved frame-
work for depression detection, introducing novel methods to extract and
interpret facial indicators associated with depressive symptoms. Through
comprehensive experiments, we demonstrate the effectiveness of our ap-
proach for real-world applications. Our findings contribute to the advance-
ment of AI-driven mental health diagnostics, offering promising avenues
for accessible and accurate diagnostic tools. This study bridges theoretical
research with practical applications, fostering the development of innova-
tive solutions for addressing the mental health crisis

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


## References

[1] Sharifa Alghowinem, Roland Goecke, Michael Wagner, Gordon Parker, and Michael Breakspear. Head pose and movement analysis as an indicator of depression. In *2013 Humaine Association Conference on Affective Computing and Intelligent Interaction*, pages 283–288, 2013.

[2] C. ´A. Casado, M. L. Ca˜nellas, and M. B. L´opez. Depression recognition using remote photoplethysmography from facial videos. *IEEE Transactions on Affective Computing*, 14(4):3305–3316, 2023.

[3] Yulia E. Chentsova-Dutton, Jeanne L. Tsai, and Ian H. Gotlib. Further evidence for the cultural norm hypothesis: Positive emotion in depressed and control European American and Asian American women. *Cultural Diversity and Ethnic Minority Psychology*, 16(2):284, 2010.

[4] Prerna Chikersal, Afsaneh Doryab, Michael Tumminia, Daniella K. Villalba, Janine M. Dutcher, Xinwen Liu, Sheldon Cohen, Kasey G. Creswell, Jennifer Mankoff, J. David Creswell, et al. Detecting depression and predicting its onset using longitudinal symptoms captured by passive sensing: A machine learning approach with robust feature selection. *ACM Transactions on Computer-Human Interaction (TOCHI)*, 28(1):1–41, 2021.

[5] J. F. Cohn, T. S. Kruez, I. Matthews, Y. Yang, M. H. Nguyen, M. T. Padilla, and F. De la Torre. Detecting depression from facial actions and vocal prosody. In *2009 3rd International Conference on Affective Computing and Intelligent Interaction and Workshops*, pages 1–7. IEEE, September 2009.

[6] Jeffrey F. Cohn, Tomas Simon Kruez, Iain Matthews, Ying Yang, Minh Hoai Nguyen, Margara Tejera Padilla, Feng Zhou, and Fernando De la Torre. Detecting depression from facial actions and vocal prosody. In *2009 3rd International Conference on Affective Computing and Intelligent Interaction and Workshops*, pages 1–7. IEEE, 2009.

[7] GBD 2019 Mental Disorders Collaborators. Global, regional, and national burden of 12 mental disorders in 204 countries and territories, 1990-2019: a systematic analysis for the global burden of disease study 2019. *The Lancet. Psychiatry*, 9(2):137–150, 2022.

[8] WHO Depression. Other common mental disorders: global health estimates. Geneva: World Health Organization, 24(1), 2017.

[9] GBD 2017 Disease, Injury Incidence, and Prevalence Collaborators. Global, regional, and national incidence, prevalence, and years lived with disability for 354 diseases and injuries for 195 countries and territories, 1990-2017: a systematic analysis for the global burden of disease study 2017. *Lancet (London, England)*, 392(10159):1789–1858, 2018.

[10] GBD 2019 Diseases and Injuries Collaborators. Global burden of 369 diseases and injuries in 204 countries and territories, 1990–2019: a systematic analysis for the global burden of disease study 2019. *Lancet (London, England)*, 396(10258):1204–1222, 2020.

[11] Asma Ahmad Farhan, Chaoqun Yue, Reynaldo Morillo, Shweta Ware, Jin Lu, Jinbo Bi, Jayesh Kamath, Alexander Russell, Athanasios Bamis, and Bing Wang. Behavior vs. introspection: Refining prediction of clinical depression via smartphone sensing data. In *2016 IEEE Wireless Health (WH)*, pages 1–8. IEEE, 2016.

[12] Hans-Ulrich Fisch, Siegfried Frey, and Hans-Peter Hirsbrunner. Analyzing nonverbal behavior in depression. *Journal of Abnormal Psychology*, 92(3):307, 1983.

[13] Wolfgang Gaebel and Wolfgang Wölwer. Facial expressivity in the course of schizophrenia and depression. *European Archives of Psychiatry and Clinical Neuroscience*, 254:335–342, 2004.

[14] J. G. Gehricke and D. Shapiro. Reduced facial expression and social context in major depression: Discrepancies between facial muscle activity and self-reported emotion. *Psychiatry Research*, 95(2):157–167, 2000.

[15] R. Islam and S. W. Bae. Facepsy: An open-source affective mobile sensing system—analyzing facial behavior and head gesture for depression detection in naturalistic settings. *Proceedings of the ACM on Human-Computer Interaction*, 8(MHCI):1–32, 2024.

[16] Rahul Islam and Sang Won Bae. Pupilsense: Detection of depressive episodes through pupillary response in the wild. In *International Conference on Activity and Behavior Computing*, 2024.

[17] Jyoti Joshi, Roland Goecke, Gordon Parker, and Michael Breakspear. Can body expressions contribute to automatic depression analysis? In *2013 10th IEEE International Conference and Workshops on Automatic Face and Gesture Recognition (FG)*, pages 1–7. IEEE, 2013.

[18] K. Koller-Schlaud, A. Ströhle, E. Bärwolf, J. Behr, and J. Rentzsch. EEG frontal asymmetry and theta power in unipolar and bipolar depression. *Journal of Affective Disorders*, 276:501–510, 2020.

[19] S. Nepal, A. Pillai, W. Wang, T. Griffin, A. C. Collins, M. Heinz, and A. Campbell. Moodcapture: Depression detection using in-the-wild smartphone images. In *Proceedings of the 2024 CHI Conference on Human Factors in Computing Systems*, pages 1–18. ACM, May 2024.

[20] Kennedy Opoku Asare, Isaac Moshe, Yannik Terhorst, Julio Vega, Simo Hosio, Harald Baumeister, Laura Pulkki-Råback, and Denzil Ferreira. Mood ratings and digital biomarkers from smartphone and wearable data differentiates and predicts depression status: A longitudinal data analysis. 2022. Preprint or unpublished work, DOI not available.

[21] World Health Organization. The ICD-10 classification of mental and behavioural disorders: clinical descriptions and diagnostic guidelines, volume 1. World Health Organization, 1992.

[22] Paola Pedrelli, Szymon Fedor, Asma Ghandeharioun, Esther Howe, Dawn F. Ionescu, Darian Bhathena, Lauren B. Fisher, Cristina Cusin, Maren Nyer, Albert Yeung, et al. Monitoring changes in depression severity using wearable and mobile sensors. *Frontiers in Psychiatry*, 11:584711, 2020.

[23] Lawrence Ian Reed, Michael A. Sayette, and Jeffrey F. Cohn. Impact of depression on response to comedy: A dynamic facial coding analysis. *Journal of Abnormal Psychology*, 116(4):804, 2007.

[24] Babette Renneberg, Katrin Heyn, Rita Gebhard, and Silke Bachmann. Facial expression of emotions in borderline personality disorder and depression. *Journal of Behavior Therapy and Experimental Psychiatry*, 36(3):183–196, 2005.

[25] Denise M. Sloan, Milton E. Strauss, Stuart W. Quirk, and Martha Sajatovic. Subjective and expressive emotional responses in depression. *Journal of Affective Disorders*, 46(2):135–141, 1997.

[26] Denise M. Sloan, Milton E. Strauss, and Katherine L. Wisner. Diminished response to pleasant stimuli by depressed women. *Journal of Abnormal Psychology*, 110(3):488, 2001.

[27] Siyang Song, Shashank Jaiswal, Linlin Shen, and Michel Valstar. Spectral representation of behaviour primitives for depression analysis. *IEEE Transactions on Affective Computing*, 2020.

[28] Michel Valstar, Björn Schuller, Kirsty Smith, Timur Almaev, Florian Eyben, Jarek Krajewski, Roddy Cowie, and Maja Pantic. Avec 2014: 3D dimensional affect and depression recognition challenge. In *Proceedings of the 4th International Workshop on Audio/Visual Emotion Challenge*, pages 3–10, 2014.

[29] A. Vázquez-Romero and A. Gallardo-Antolín. Automatic detection of depression in speech using ensemble convolutional neural networks. *Entropy*, 22(6):688, 2020.

[30] Rui Wang, Andrew T. Campbell, and Xia Zhou. Using opportunistic face logging from smartphone to infer mental health: Challenges and future directions. In *Adjunct Proceedings of the 2015 ACM International Joint Conference on Pervasive and Ubiquitous Computing and Proceedings of the 2015 ACM International Symposium on Wearable Computers*, pages 683–692, 2015.

[31] Y. Xing, N. Rao, M. Miao, Q. Li, Q. Li, X. Chen, and J. Wu. Task-state heart rate variability parameter-based depression detection model and effect of therapy on the parameters. *IEEE Access*, 7:105701–105709, 2019.
