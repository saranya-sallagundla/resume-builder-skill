# Static scorer served by nginx. Multi-stage keeps the final image tiny (~10 MB).
FROM alpine:3.20 AS build
WORKDIR /src
COPY web/ ./web/
COPY examples/sample_jd.md examples/sample_resume.md ./web/

FROM nginxinc/nginx-unprivileged:1.27-alpine
COPY --from=build /src/web/ /usr/share/nginx/html/
EXPOSE 8080
HEALTHCHECK --interval=30s --timeout=3s CMD wget -qO- http://127.0.0.1:8080/ >/dev/null || exit 1
