docker


docker build -t hostile-tweets-ex .
docker login
docker tag hostile-tweets-ex yitzchakdamen/hostile-tweets-ex:v4
docker push yitzchakdamen/hostile-tweets-ex:v4

----

k8s

oc login ????

oc  apply -f configmap.yaml
oc  apply -f secrets.yaml

oc apply -f deployment.yaml
oc apply -f service.yaml
oc apply -f route.yaml

-----