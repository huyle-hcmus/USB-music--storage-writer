# USB Music Storage Writer
### Project uses kit STM32
1. Configure the UART protocol to transmit any music data on the computer to the STM
2. Configure the USB host to write the music file data to USB storage.

### Kit Open405R-C Package A, STM32F4 Development Board
![Open405R-C-1](https://i.imgur.com/DQVrHfb.jpg)

### Describe
- Configure UART and USB to transmit data from the computer to the STM32 board and store data in USB.
- Run the python file music.py to transfer the music data to be transmitted (identification sign: LED light changes state: from off to bright).
- Data will be saved into the buffer variable
- Finally, the board will create a file on the USB from the above data and save the data there.

### System Config
**1. Configure code compilation onto the board according to Serial wire standards.**
![config_1](https://github.com/huyle-hcmus/step-counting-device/assets/132913421/8678cf5c-0cfd-467d-adf7-68db98e43baf)

**2. Use Crystal/Ceramic Resonator.**
![config_2](https://github.com/huyle-hcmus/step-counting-device/assets/132913421/f776eb8b-b380-4168-85b8-a2c570acdba5)

**3. UART Config**
![uart_config_1](https://github.com/huyle-hcmus/step-counting-device/assets/132913421/beb1a1a8-c176-458f-9b04-e23c4822c02a)

**4. USB Config**

*4.1. Configure USB_OTG_FS, select Host_only mode and tick Activate_VBUS.*
![usb_config](https://github.com/huyle-hcmus/step-counting-device/assets/132913421/352ec470-56f7-444c-99a2-82ab0ff68ddf)

*4.2. USB_HOST Config*
![usb_host_config](https://github.com/huyle-hcmus/step-counting-device/assets/132913421/f0130782-3475-4e01-97a2-73b41d8f8a7e)

*4.3. FATFS Config*
- ![fatfs_config](https://github.com/huyle-hcmus/step-counting-device/assets/132913421/bbff8832-bc36-4339-96b6-5f26654f01a5)

- ![fatfs_config_2](https://github.com/huyle-hcmus/step-counting-device/assets/132913421/5d1e5b05-d566-456b-bff4-5df241f6654f)

### Contributors
- HUY LE
- HUY HO
- KHANH NGUYEN

### See results in part V, page 30 in [report](https://github.com/huyle-hcmus/embedded-system/blob/main/project__docs/TH_HTN_K20.pdf)
