t=[0:0.1:20];
wt=(exp(t/5.0)-1)/30+1;
plot(t, wt);
xlabel("time index t (fault at index 0)");
ylabel("delay factor");
title("(exp(t / 5.0) - 1) / 30 + 1");
print ("-dtex", "failure_profile.eps")
print ("-deps", "failure_profile.eps")

t=[1:12];
rd=poissrnd((exp(t / 5.0) - 1) / 4) * 0.2 + 1;
t2=[1:0.1:12];
md=((exp(t2 / 5.0) - 1) / 4) * 0.2 + 1;
plot(t, rd, "*", t2, md, "-");
xlabel("time index t (fault at index 0)");
ylabel("delay factor");
title("poissrnd((exp(t / 5.0) - 1) / 4) * 0.2 + 1");
legend("Sampled random delays from Poisson", "Mean delay profile");
print ("-dtex", "retry_profile.eps")
print ("-deps", "retry_profile.eps")


