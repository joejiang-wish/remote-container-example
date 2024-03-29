# Intro
Developing within docker container is great, but still have problems such as how to do code jump to third part lib. The vscode-remote-containers handle this.

If you want to setup remote container on your container instead of this example, move to [setup-remote-container](#setup-remote-container-and-enable-code-navigation)

This project is an example of how to use vscode-remote-containers with `python2` Language, `tornado` 3 part lib.


# Start this project by vscode-remote-containers

## Setup by [devcontainer.json](https://code.visualstudio.com/docs/remote/devcontainerjson-reference)(RECOMMENDED)

1. Declare `.devcontainer/devcontainer.json` at root of your project. (skip this step since devcontainer.json is prepared.)

    ```json
    {
    "language": "python2",
    "path": "./",
    "container": "python2-tornado-container",
    "container_args": [
        "--port",
        "8888"
    ]
    }
    ```

2. open the Command Pallette(macos `shift+command+p`) and click `Remote Containers: reopen container`

## Setup manually

1. At host machine run `make dev`(`docker-compose up`) to ensure container started.
2. Install the [Remote - Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) extension
3. In any vscode window, open the Command Pallette(macos `shift+command+p`) and type `Remote-Containers`, then select the `Attach to Running Container...` and select the running docker container.

    Note: You should keep the container running for the extension to work. In addition, name the container meaningful so you can find it easily.
    
    ![Untitled](assets/attch-container.png)
    
4. VScode will open a new blank window with the remote container.
5. On the `Explorer` sidebar, click the `open a folder` button and then enter `/root/app` (this path is under the container)

    Note: `/root/app` maybe different in your container. Here because the example container running with the volume mapping `.:/root/app`, check at [docker-compose.yaml](docker-compose.yaml)

    ![Untitled](assets/open-code-folder.png)
    
6. On the `Extensions` sidebar, select the `Python` extension and install it on the container

    ![Untitled](assets/install-python-extension.png)

7. open the Command Pallette(macos `shift+command+p`) and select interpreter, select `/usr/local/bin/python` (If the app start by virtualenv in container, please select the correct python PATH.)

    ![Untitled](assets/select-interpreter.png)

8. Wait a while, after that(vscode need some time to build all the links, big project may get longer) and you can try to navigate the code definition.

9. Open terminal(Macos `control + ~`) in vscode, and the terminal is the container shell. Easy to run command in the container.

## Q & A

- Close the remote-container vscode and reopen it, do I need to do the setup steps again?

    No.

- Restart the container and, do I need to do the setup steps again?

    No.

## About hot-reload process
Recommend to use [`nodemon`](https://github.com/remy/nodemon), although it needs the nodejs environment.
It can watch multiple language files and reload the file when it changed.

nodemon can also be used to execute and monitor other programs. nodemon will read the file extension of the script being run and monitor that extension instead of .js if there's no nodemon.json

## Enable git commit hook
TODO