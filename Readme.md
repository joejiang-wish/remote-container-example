# Intro
Developing within docker container is great, but still have problems such as how to do code jump to third part lib. The vscode-remote-containers handle this.

This project is an example of how to use vscode-remote-containers.

Language is python2, lib is tornado.

## Steps
1. At host machine run `make dev` to ensure container start
2. Do the following setup guides.

## Setup remote container and enable code navigation
1. Install the [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python) extension
2. Install the [Remote - Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) extension
3. Open the Command Pallette and type `Remote-Containers`, then select the `Attach to Running Container...` and selecet the running docker container
    
    ![Untitled](assets/attch-container.png)
    
4. VS Code will restart and reload
5. On the `Explorer` sidebar, click the `open a folder` button and then enter `/root/app` (this will be loaded from the remote container)

    This because the container running with the volume mapping `.:/root/app`, check at [docker-compose.yaml](docker-compose.yaml)

    ![Untitled](assets/open-code-folder.png)
    
6. On the `Extensions` sidebar, select the `Python` extension and install it on the container
    
    ![Untitled](assets/install-python-extension.png)
    
7. MACOS `shift+commad+p` and input “select interperter” , select `/usr/local/bin/python` (If the app start by virtualenv in container, please select the corrent python path.)
    
    ![Untitled](assets/select-interpreter.png)
    
8. Wait a while(vscode need some time to build all the links, big project may get longer), after that and you can try to navigate the code definition.

9. Macos `control + ~`  can open terminal in vscode, and the terminal is the container shell

## Q & A

- Close the remote-container vscode and reopen it, do I need to do the setup steps again?

    No.

- Restart the container and, do I need to do the setup steps again?

    No.

## Enable git commit hook
TODO