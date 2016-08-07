load("data.mat")
[x,y] = find(data);
S(x)=y;
plot(S, "k+");
xlabel("index");ylabel("event type");

