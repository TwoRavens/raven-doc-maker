We have two TA3 containers that need require to the shared volume. It appears that these shared volumes are only added to the ta2main and ta3main.

For each container that needed volume access (2 TA3s and 1 TA2), we added this annotation from the submit guid3:
```
    - mountPath: /shared_dir
      name: shared-vol
      readOnly: false
```


line 26
- line 26 of script looks for container name `ta2main`, submission example uses `ta2-main`
- line 31 of  looks for container name `ta3main`, submission example uses `ta3-main`

lines 29 and 34
- does the pod itself, need the labels `ta2main` and ta3main`.  It looks like the script crashes if they're not present.
