% Try1

a=212;
b=255;
c=a+b

%% Try 2 (a)

a=[1 2 3 4 5]
%% Try 2 (b)

a(3)
%% Try 3 (a) 

length(a)
%% Try 3 (b) 

size(a)
%% Try 4

f=[1 2 3 4 5 6]
f(4)= 60

%% Task 1 (i)

x=[ 2,4,5,9]
x.*x
%% Task 1 (ii)
x.^2
%% Task 2(a) (i)
a = [2 5 3 ; 1 1 0; 9 6 -1];
b = [ -1; 6; 9];
c = [3 -2 4];

a*b

%% Task 2(a) (ii)
 a + 4


%% Task 2(a) (iii)
 %z = b*a
 %% Task 2(a) (iv)
c.^2

 %% Task2(b) (i) 
 a= [3 1 4];
 b = [4 2 3];
a.'

 %% Task2(b) (ii) (a) (b)
 bt = b.';
 a1 = a*bt
 b1= b*at

 %% Task2(b) (iii) (a) (b) 
 a2 = bt*a
 b2 = at*b

 %% Try 5
A= [1 2 3] 
B= [2 3 6] 
C= [A B] 
%% Try6

x=-2:0.1:2; 
%start_step:step_size:end_step
y = x.^2; %{ Element wise
%multiplication operation %
plot(x, y)
title('Plotting y(x)');
xlabel('x-axis'); 
ylabel('y-axis');

%% Task 3
f1 = 3;
dt = 1/(30*f1);
dm = 4/(f1);
t = 0:dt:dm
x = sin(2*pi*f1*t);

plot(t,x)
title("Plot x for f=3Hz");
xlabel('time'); 
ylabel('amp');
%% Task 3
f1 = 300;
dt = 1/(30*f1);
dm = 4/(f1);
t = 0:dt:dm
x = sin(2*pi*f1*t);

plot(t,x)
title("Plot x for f=300Hz");
xlabel('time'); 
ylabel('amp');

%% Task 3(ii)
a1 = 0.01;
dt = 1/(30*a1);
dm = 4/(a1);
t = 0:dt:dm
x = 1-exp(-a1*t);
plot(t,x)
title("Plot x for a=0.01");
xlabel('time'); 
ylabel('amp');
%% Task 3(ii)
a2 = 100;
dt = 1/(30*a2);
dm = 4/(a2);
t = 0:dt:dm
x = 1-exp(-a2*t);
plot(t,x)
title("Plot x for a=100");
xlabel('time'); 
ylabel('amp');
%% Plotting 1st function 
subplot (3,1,1) %1st
plot x=-3:1:3; m = x.^2;
plot(x,m,'k','LineWidth',2.5)
title('Plotting m(x)');
xlabel('x'); ylabel('Amplitude'); 

% Plotting 2nd function
subplot (3,1,2) %2nd 
plot x=-3:0.1:3;
n = 2.5*(x.^2);
plot(x, n,'r') title('Plotting n(x)');
xlabel('x');
ylabel('Amplitude');

% Plotting 3rd function 
subplot (3,1,3) %3rd
plot x=-5:0.01:5; p= 2*(x.^2); plot(x, p,'g*')
p(x)'); xlabel('x');
ylabel('Amplitude');
%Adding main/super title suptitle (‘Non-linear graphs’) 
%ignore this command if gives error 

%% Plotting 1st function 
x=-3:1:3;
m = x.^2; 
plot(x,m,'k','LineWidth',2.5) title('Plotting m(x)');
xlabel('x'); ylabel('Amplitude'); 
 
% Plotting 2nd function figure 2nd window 
x=-3:0.1:3; 
n = 2.5*(x.^2);
plot(x, n,'r') title('Plotting n(x)');
xlabel('x'); ylabel('Amplitude'); 
 
% Plotting 3rd function Figure %3rd window 
x=-5:0.01:5;
p = 2*(x.^2); 
plot(x, p,'g*') title('Plotting p(x)'); 
xlabel('x'); ylabel('Amplitude');

%% Plotting 1st function 
x=-3:1:3; 
m = x.^2; 
plot(x,m,'k','LineWidth',2.5) title('Plotting m(x)');
xlabel('x'); ylabel('Amplitude'); 
 
% Plotting 2nd function 
x=-3:0.1:3; 
n = 2.5*(x.^2); 
hold on
plot(x, n,'r') title('Plotting n(x)'); 
xlabel('x'); ylabel('Amplitude'); 
 
% Plotting 3rd function 
x=-5:0.01:5;
p = 2*(x.^2);
plot(x, p,'g*') title('Plotting p(x)'); 
xlabel('x'); ylabel('Amplitude'); 
axis([-3,3,0,40]) legend('m','n','p') 
hold off

%%
a=[rand(1,2) ones(1); zeros(1) eye(1,2)] %zeros,ones,eye and rand to create a matrix. b=[zeros(2,1) eye(2)] %matrix eye(2) as part of 2 × 3 matrix. size(a) %Verify the sizes of your arrays using size. 
size(b) 

%%
zeros(1,36) 
x(18) = 1


