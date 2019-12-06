#!/usr/bin/env python3
from rak811 import Mode, Rak811

lora = Rak811()
lora.hard_reset()
lora.mode = Mode.LoRaWan
lora.band = 'EU868'
lora.set_config(dev_eui='xxxxxxxxxxxxxxxx',
app_eui='xxxxxxxxxxxxxxxx',
app_key='xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
lora.join_otaa()
lora.dr = 5
lora.send('Hello world')
lora.close()
