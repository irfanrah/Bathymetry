x = [-4.22   4.24   4.242333   4.422   4.22  4.21   4.21   4.25   4.21    4.24];
y = [0,0,-2,-2,-2,-5.8,-7.4,-9,-10.7,-12.2];
z = [1028,1028,1012,980,951,931,907,900,888,883];

x1 = xlsread('olda.xlsx','d3:d2502') ;
y1 = xlsread('olda.xlsx','c3:c2502') ;
z1 = xlsread('olda.xlsx','n3:n2502') ;

x2 = reshape(x1,[1,2500])
y2 = reshape(y1,[1,2500])
z2 = reshape(z1,[1,2500])


xv = linspace(min(x2), max(x2), 50);
yv = linspace(min(y2), max(y2), 50);
[X,Y] = meshgrid(xv, yv);
Z = griddata(x2,y2,z2,X,Y);
contourf(X,Y,Z)
grid on
shading interp
hold on
scatter(-6.3626358, 106.8261662,[],'k')