
X = [0.69, -1.31, 0.39, 0.05, 1.29, 0.49, 0.19, -0.81, -0.31, 0.71];
Y = [0.89, -1.11, 0.59, 0.45, 1.19, 0.69, 0.25, -0.71, -0.21, 0.71];
x = mean(X);
y = mean(Y);

x1 = [x, x, x, x, x, x, x, x, x, x];
y1 = [y, y, y, y, y, y, y, y, y, y];

mat = [(X-x1);(Y-y1)];
mat1 = transpose(mat);
result = 1/10 * mat * mat1;
r = corr2(X,Y);

lamba = eig(result);

% Get the eigen-vectors
[V,D,W] = eig(result);
MAT = W * mat;
MAT1 = transpose(MAT);
RESULT = 1/10 * MAT * MAT1;

% calculate A and B using the new basis
f1 = [-0.7253, -0.6885] * [0.05;0.45];
f2 = [-0.7253, -0.6885] * [0.49;0.69];
y2 = 0.9493 * X + 0.143;
y3 = -1.0534 * t + 0.4194;

% plot A and B in sub-(f)
plot(0.05,0.45,'y')
plot(0.49,0.69)
xlabel('x')
ylabel('y')
hold on

% plot two vectors representing principal components
quiver(0.0,0.0,-0.7253,-0.6885)
xlabel('x')
ylabel('y')
hold on

quiver(0.0,0.0,0.6885,-0.7253)
xlabel('x')
ylabel('y')
hold on

% plot A and B
A = [0.05;0.45];
B = [0.49;0.69];
scatter([0.05,0.49],[0.45,0.69],'filled','r');
xlabel('x')
ylabel('y')
hold on

% plot all data points
scatter(X,Y)
xlabel('x')
ylabel('y')

