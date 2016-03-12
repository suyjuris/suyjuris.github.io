j,k=exec,'scipy.interpolate scipy.signal numpy c'
l,c,h,r='airo tkinter',256,'w.set_line_','photo'
for i in(k+l).split():j('from %s import*'%i)
def q(x,y,m=splev,A=splprep,B=sqrt,C=firwin):
 x,y=array(x)/99.,array(y)/99.;g=A([x,y],s=0,k=1)
 z,o=x[1:]-x[:-1],y[1:]-y[:-1];t=sum(B(z*z+o*o))
 n,b=200*t,C(60,.03*t,None,30);x,y=m(f(n)/n,g[0])
 z,o=x[2:]-x[:-2],y[2:]-y[:-2]
 d,p=random.normal(0,.01,len(z)),B(z*z+o*o)
 a=lfilter(b,1,d)/p;x,y=x[2:]+a*o,y[2:]+a*z
 [w.line_to(*i) for i in zip(x,y)];w.stroke()
f,s=arange,ImageSurface(0,c,c);w=Context(s)
w.scale(c,c);w.set_source_rgb(0,0,0);v='join(1)'
j(h+'cap(1)');j(h+v);h+='width(.0';j(h+'4)');q([3
,14,31,42,96,96],[51,46,84,15,15,22]);j(h+'3)')
q([56,66,78],[81,57,81]);q([66,66],[57,41]);q([52
,66,80],[53,41,53]);u=f(17)*.4;q(sin(u)*9+66,cos(
u)*9+32);s.write_to_png(r);Tk();i=Image(r,file=r)
Label(image=i).pack();input()
