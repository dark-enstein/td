title: "Node.js Deployment"
wrangler: "alex"
stock: "nodejsapp/server"
#flags:
#    - "auto-restart"
rodeos:
  - rodeo:
      - ranch:
          name: "Clone Repository"
          cmd: [ "git", "clone", "https://github.com/user/nodejsapp.git" ]
      - ranch:
          name: "Install Node Modules"
          cmd: [ "npm", "install" ]
      - ranch:
          name: "Run Tests"
          cmd: [ "npm", "test" ]
      - ranch:
          name: "Start Server"
          cmd: [ "npm", "start" ]
