# discord-thermometer

Creates a personal discord bot that can report on the current temperature of the room by polling a Raspberry Pi wired to a DS18B20 digital thermometer.


This project uses virtualenv (python3) to manage packages. Install packages with

```shell
python3 -m venv <myenv>
source <myenv>/bin/activate

pip install -r requirements.txt
```

## To-Do
- Fix errors causing program shutdown
