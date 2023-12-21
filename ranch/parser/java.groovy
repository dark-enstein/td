title: "Java Maven Build"
wrangler: "natalie"
stock: "javaproject"
#flags:
#    - "skip-tests"
rodeos:
  - rodeo:
      - ranch:
          name: "Clean Build"
          cmd: [ "mvn", "clean" ]
      - ranch:
          name: "Compile Code"
          cmd: [ "mvn", "compile" ]
      - ranch:
          name: "Package Application"
          cmd: [ "mvn", "package" ]
      - ranch:
          name: "Deploy Artifact"
          cmd: [ "mvn", "deploy" ]
