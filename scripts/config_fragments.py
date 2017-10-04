
RAVENS_ISI_VOLUME_MOUNTS = '''
        - mountPath: /shared_dir
          name: shared-vol
          readOnly: false
        - mountPath: "/ravens_volume"
          name: "ravens-volume"
          readOnly: false
        - mountPath: /tmp/dsbox-ta2/
          name: "isi-volume"
          readOnly: false'''

RAVENS_CRA_VOLUME_MOUNTS = '''
        - mountPath: /shared_dir
          name: shared-vol
          readOnly: false
        - mountPath: "/ravens_volume"
          name: "ravens-volume"
          readOnly: false'''
