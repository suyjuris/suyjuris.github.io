k='scipy';j=exec;F='w.set_line_','photo','cap(1)'
k+='.interpolate %s.signal numpy cairo tkinter'%k
for i in k.split():h,r,l=F;j('from %s import*'%i)
def q(x,y,A=array,B=sqrt,C=random.normal,G=None):
 D=x,y=A(x)/99,A(y)/99;z,o=x[1:]-x[:-1],y[1:]-y[:
-1];n=sum(B(z*z+o*o))*c;x,y=splev(f(n)/n,H(D,s=0,
k=1)[0]);z=x[2:]-x[:-2];o=y[2:]-y[:-2];a=B(z*z+o*
o)/lfilter(E(60,n/7e3,G,30),1,C(0,.01,len(z)));[J
(*i)for i in zip(x[2:]+o/a,y[2:]+z/a)];w.stroke()
c=200;s=ImageSurface(0,c,c);w=Context(s);w.scale(
c,c);E=firwin;f=arange;j(h+l);J=w.line_to;Tk();j(
h+'join(1)');H=splprep;h+='width(.0';j(h+'4)');q(
[3,14,31,42,96,96],[51,46,84,15,15,22]);j(h+'3)')
q([56,66,78],[81,57,81]);q([66]*2,[57,41]);q([52,
66,80],[53,41,53]);u=f(17)*.4;q(sin(u)*9+66,cos(u
)*9+32);s.write_to_png(r);i=Image(r,fi=r);Label(i
=i).pack();input()#Python3, Numpy, Scipy, PyCairo
