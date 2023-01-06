
# FROM golang:1.19.4-buster  AS build

# WORKDIR /app

# COPY go.mod ./
# COPY go.sum ./
# RUN go mod download

# COPY . ./

# ENV GOARCH=amd64 GOOS=windows

# RUN go build \
#     # -ldflags "-X main.buildcommit=`git rev-parse --short HEAD` \
#     # -X main.buildtime=`date "+%Y-%m-%dT%H:%M:%S%Z:00"`" \
#     -o /go/bin/app


# ## Deploy
# FROM gcr.io/distroless/base-debian11

# COPY --from=build /go/bin/app /app

# EXPOSE 8080

# USER nonroot:nonroot

# CMD ["/app"]


FROM golang:1.19.4-alpine

RUN apk --no-cache add make git gcc libtool musl-dev ca-certificates dumb-init 


# Set the Current Working Directory inside the container
WORKDIR /app/go-sample-app

# We want to populate the module cache based on the go.{mod,sum} files.
COPY go.mod .
COPY go.sum .

RUN go mod download

COPY . .

# Build the Go app
RUN go build -o ./out/go-sample-app .


# This container exposes port 8080 to the outside world
EXPOSE 8080

# Run the binary program produced by `go install`
CMD ["./out/go-sample-app"]