% import Data-Q2.txt 
filename = '/Users/quanwan2/Desktop/data/Data_Q2.txt';
delimiter = '\t';
formatSpec = '%s%s%s%s%s%s%s%[^\n\r]';
fileID = fopen(filename,'r');
dataArray = textscan(fileID, formatSpec, 'Delimiter', delimiter,  'ReturnOnError', false);
fclose(fileID);



% We get all 7 columns as 7 arrays
ID = dataArray{:, 1};
City = dataArray{:, 2};
State = dataArray{:, 3};
Category = dataArray{:, 4};
Price = dataArray{:, 5};
Quarter = dataArray{:, 6};
Year = dataArray{:, 7};

clearvars filename delimiter formatSpec fileID dataArray ans;

% b
A1=strcat(City, Category, Price, Year);
B1=unique(A1);
[row1,col1]=size(B1);
fprintf('For the given condition, there are %d distinct cells in the cuboid.\n',row1);

% c
A2=strcat(State, Category, Price, Year);
B2=unique(A2);
[row2,col2]=size(B2);
fprintf('For the given condition, there are %d distinct cells in the cuboid.\n',row2);

% d
A3=strcat(Category, Price, Quarter);
B3=unique(A3);
[row3,col3]=size(B3);
fprintf('For the given condition, there are %d distinct cells in the cuboid.\n',row3);


% e
A4=strcat(State, Category, Quarter);
Court1=sum(strcmp(A4, 'IllinoisfoodQ1'));
fprintf('For e, the count for the cell is %d.\n',Court1);

% f
A5=strcat(City, Price, Year);
Court2=sum(strcmp(A5, 'Chicagocheap2013'));
fprintf('For f, the count for the cell is %d.\n',Court2);
