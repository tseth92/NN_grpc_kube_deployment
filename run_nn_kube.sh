kubectl apply -f kube/pv.yaml
kubectl apply -f kube/pvc.yaml
kubectl apply -f kube/nn-sq-train/nn_sq_train_svc.yaml
kubectl apply -f kube/nn-sq-predict/nn_sq_predict_svc.yaml
kubectl apply -f kube/nn-sq-train/nn_sq_train_deployment.yaml
kubectl apply -f kube/nn-sq-predict/nn_sq_predict_deployment.yaml
