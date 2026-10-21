`ca-certificates.crt` is mounted over the CA bundle of both containers. It is the
bundle of Alpine 3.24 (from `grafana/grafana:13.2.3`) without
emSign ECC Root CA - G3, which chains to eMudhra's compromised intermediates
(https://emudhra.we-have-a-problem.com/). Drop the mounts once both images ship
a `ca-certificates` without that root.
