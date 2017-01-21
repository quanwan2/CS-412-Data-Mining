scores = load('/Users/quanwan2/Desktop/data/data.online.scores');
finalScores = scores(:, 3);
Q1 = quantile(finalScores,0.25);
Median = quantile(finalScores,0.5);
Q3 = quantile(finalScores,0.75);
Mean = mean(finalScores);
Mode = mode(finalScores);


