# YOLOv8-Based Real Time Weapon Detection System for Jetson Nano 



## Installation
• Get a 32 GB (minimal) SD card to hold the image.  
• Download the image [JetsonNanoUb20_3b.img.xz](https://ln5.sync.com/dl/403a73c60/bqppm39m-mh4qippt-u5mhyyfi-nnma8c4t/view/default/14418794280004) (8.7 GByte!).  
• Flash the image on the SD card with [balenaEtcher](https://etcher.balena.io/) after format.  
• Insert the SD card in your Jetson Nano .  
• Password: `jetson`



## Usage
```terminal
python3 -m pip install ultralytics
git clone https://github.com/HarcheSamir/Yolov8JetsonNano
cd Yolov8JetsonNano
python3 vidTest.py # or webCam.py to use with attached cameras
```  

## Pre-installed software

![Alt text](
data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAkGBwgHBgkIBwgKCgkLDRYPDQwMDRsUFRAWIB0iIiAdHx8kKDQsJCYxJx8fLT0tMTU3Ojo6Iys/RD84QzQ5OjcBCgoKDQwNGg8PGjclHyU3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3N//AABEIAJQBAAMBEQACEQEDEQH/xAAaAAACAwEBAAAAAAAAAAAAAAADBAIFBgEA/8QAPBAAAQMDAwIEBQEFBgcBAAAAAQACAwQRIQUSMUFREyJhcQYUMoGRoSM0scHwJDNCUmLRFkNTcoLh8RX/xAAbAQACAwEBAQAAAAAAAAAAAAACAwEEBQAGB//EAC8RAAICAgIBBAIBAgYDAQAAAAABAhEDBBIhMQUTIkEyUWFxkSMzQoHw8UOx0Qb/2gAMAwEAAhEDEQA/AE4XLXTPWtDsJRimM8tVDYRC8gz5brKkN+gb32KAlIiHXFkDBaIOblKbBDQNSZMCQ6xqSJYZoRoFkXJyCSONbdGgzkosLJsQooRlZcpqZYiCEF06LCs8YrHOExMOxmIAN5TosW0DeAXcog0hiNrQ3KJMBplbXgZspbH4heDyZUpjJKxh9QLcj8ouQtQEqma/CFyGxiVm93iZ4Q2WOKovdMLnABoKKJSzpGlo6Z7gLgj7JhmZZpeC3hgDGYXFKUrZGok2NUoiPZXyyWbcZKm6GqNsUqZHvjshcx8MaTtgWSTMZttgLlMKUYNkzWSN23Bt7KeYPsxZmoX25KYmaDQ7FJxlMsU0ORvuFWzICjpWPlVMYgUjUmybBhCyGe6pUgaGacJEhch1gSxTCI4kUBkvdPiMijsZ5RpBUclGE1IOKFiADlMiNQVgZYXCcgXYtOL8JiGxR6K5Fk6JLRN0TmnzNI9wiaIjKL+yL3FrbKLCpWIyAvJuF1jVSFnBzcWUphqmAkc6+ApsJJEWgu5XHBaSiNTLtABClICeXijY6TpMcTBdqYujIz7Dky5DWRiwCmyk7ZF0mOy4ihKqcXg2OAFLGY1XkQja4klxwhsfJpeCBIdM5t8AKDk+jxIs/uFFkLsA6UEhrhZdYai/oyrH2TUzTocgfeyamBKI9FJhLy+BLQXxMLIzLsJIFLLhViVEA2a5tlQ0E4B2G6RJi2h2AWVebEyGgbIYoXR0PF01IniefkJyDiiDBYlNiHRJ9rJiJSFZMEo4odFATIRhOXQahZJsFRNmKGRw7hpsmKMv0BLPhx/lNL/ctNEhiifPPWjaIG3Id0PqrmLFKkzD9V9Vxxh7eKVhG+JW3kbE8wuN2Etsi2IStUjG0d948nyl0KVtJJDcyROa3vbCruLS8HrsO1izfhJP/cqpNvcIC4BkYEaJTYrI0BSMTBEgcKSGaDQoB5XWyUUSjszo1cfljARmW+2RcblccLVTjYNYcqWwsat9ldUTyNaYwPMULY5QT7AASbLOdZD2E3EAY5GO3A3uhdhKUWqOwS75zu4HKi7Z0o1EJO1krg3qOyIXGTRiBLYptm2ojdPMMJkWLlEfjkwun4EuIw03Cyc6JojKDZU7JQuxp3KJMljkPCRNimPxYVWQmSCE4RRISONJunIKgl8JiJSIE2TYjEiJkvjqmImvsYbDHCI36gyRkch2tLXAEE9SFZwxjJ1JlHb2p448sKTotI4KShzDF8w+wJe8+b3AstPDggjyvqXq+5mfGHUf4F5PiaB25w3WabDc3ab+1r/i6srE/pHn5bXdSMbqWsSVDpQPG/bOGNxw4ZA7H8phYjJcLNFp+vtZAyFrSZCANjQbk+mOfRDKLKqzy8R7Laorn08AqK+RsVO0ZBN3OPa3AP3SZyhFF/Uw7GSacev9zPzCava6opdKkhiHmDw+5I9W3v8Aos33sblxR7vS2MsWoZZX/X/6VTpL3tdMNriLyPUk0CZd7w0dSuJfSNpokQaxt+yOJkbDst3OxhGVKATSkYacqLDjETkqGRtJcfMFFhOLfgTbL4rjIehwutMKS4qgMtRyTyobIULBfNtA+oIG0GsbF4pm+O8g2ulqSsc4viFbK7xC5p4RWL49GILk9M3aD07iCESYEkWtO7GUT8FaQ9G6wWZsAUFJBCz2yKBgAOQtkjEXKRNi2NsKSLomUUSUjzcFOQVBL4wmI6gcnF0yIcQ0F4NpEHiTyZaDuu0fYHJ/gnSxTWPn9GXs72JZXiUu0IayKiRr2ylzWkZDnX2n35PsUGDKrtkQzR4+Auj1z63T4bOAlaNhzfjp+f66LewzUopnl97A4zkkFfF8xGJHwuDbWfYNx17q0stOrPKbPObUkvH/AD9C0ekRueTY7S7LWAn9OEU8iStEY82WS4u/7f8ARcQU7qWMMgDRj+8A4736pXu8lZf18M01GuzM6vXmv1ERRWLInWY0nF+S446D9VQzZlE9vo4VBKT8FjR1NTDnbL5RfkA27k5/A/KxcvydmjKcX+v+fwA1Y01ZCamB2ydg3SRuABkHcEYPf2BVrWnkT45C3p56lwl4KN9rcq8atB9MiMtSOwXWJyukbWiHhxhMiZOX5MLNLsGMomwIwtiu8kl5NlAcqSpCkmySQ3Nyo6BUmkVk0xgmIP0nslykkOUeaBt3VG4g2SXO/AylDyQhijLnB5yEtsKUuujzIm2fYm98IOzuZ6HeXFoPC5TZLcasz2n6XV15/s8ZcO6uyywh5Zey54YvyY/U6HW0MYknjszqQeEWPYhN0hOPbx5XUSED7BWJPoKSHGP4Wbn7BoYY7CzZeQSQ5QNkMPCkSAYyxLsCggRI4442TYhpHmOymoKjsjwGFHF9nRTspfiTW9UooZJtIqDG1kux5Ddz2YwAey280IZccV/B4LDjlj2cjzL5W/8A2If8RP1bRIanUWf2gF0cjmYEu3r+qx5a0cWSoeDRhlmlUSy+FnhwkDA9oc5127N23Pf+j7LdwQ4xSKm1JvuT7o0tmufvjfuF9oJa647+U8H/AMlcrl5R5bPieKbp9HY2ENcD4htexkZk46G5P4C7hH6QmKlJU2/7f9kNRqWMoneFI1u4XcDZzhjm3b3VfK6R6L0/XjGoxMLFJ4NU+SSQsN7jqSbn/ZZexCXk9G83B8YqxvV/jeq0WSlotNiY6R0Ye+eRu4uJPFlUhqRyW5CJzTl8l0ywotUNeIZqiFsLp2Zp+jicbh6H+C18McahT8laMNiOzD2n1a/sVElxZvVJs9+nasvdBpiAHEZK5FLYmaAybG2TbKHGxaasZe18qOQz22hOeqAZYHN13IDj2KiQ/XfhC5BV9Am2nm3OHlCrynbDXxQCWTZI4MwOyBumTd+ReMPe8m5F0PKwrHCNjL3QuQpPsjFckkIOXYx+C70Gan0+ljYAL27LF296fu9Gftcsk7Zz4qq2z6a4xkH+Su+l5/cyh6EXHIYyM5wvTSfRuMcj6LNzMAaYbBUJMBhG5SpEMYiKSwGHaUJFE9yJI6jznXCag0iIKYgqISux6o0FFdgKrT9VbTOq4Kds0AbZ8RZe/rbr0Whh2FXFumec9U0sEsjyRfbMlqFXLVyhoZDHG0WZFE3axoueibDFc7KMYQhEvtF3w0rXl5ZY7twbfkZNlqyxuMEzMWaOTNLGjUsfPs3yRPkBZtLmysksfs3Pt+qKNMy9qDirUQjXynJgmexguS14NrdM3IHv+FM6RX1cU8kk5IoNSqTWTPuAxrLuAsCSbYyMdOypyfOaR6zFBYMTmZrU2ObK/AIfchw59f67ErtnG4uhujlWWKlfZOGWmqYo/nqJk5j/ALt1yLDsbcgLNU5QbVItS1VKV2afQKGeomfW1XgtaRaJo7dLey0NfE3U5lLd3YYKxYvP2crtFvU+LG9u2+RZJyK5dG5pes4pY1CXktqSFtPD7KF0WJT5voFLOC4gnCXKQaVIqKwOY4vY42QcmMjJPpiscktQ8dG3sSu5NnOKQeoIiswPvdBKbsFJMFHOBhp4Q2iJhWU88j/Fjglew9WtuFEuT8IQ8mOPTkkMUemVVZVeFHE6Mcl72kABdjxZJypC821iww5N3/Rl9/8AhaWHtgmnnMgy524D9LK+tCLXkzVv7MlyjFDUHw9pTLtMkzic33gY/CBaEPsGXqWz54oyFM5z4WXXjdmKWRmtlj8huaDxtMkB6Ap3p2VQzgYZcciMnCfPbthexlLo3ZLosovpWXml2JYdqqNkBY0qTBYwxIYAUFciDm5OQaRIORolHWm6Mki8tbYnoUaCSs22k17WULABmyxNzbnimkjD2MNzbMlX/BcXzr5qeqDmvdu2vjNgev6r3GDO7txPP518XFOmL1+izwU+1ko8oy4dQPTstB5YZVT6MfHjy6+TnF3YjRGphlMZrGwxuBuxzL+t8mwPrZV5VF9Po0vlljfDsNXzTus2Cuilbi7WR2t7cWHoonK/sdr4uHcoAKLT6mZwIdZptdpP81EIRi7YzNmyTXHwMVWhumA8zCLA2J/XHv8AxTMmZS8oTqY/a6TO6b8GOdNFLUVsUcJN5G7gXW/Cx8mw038DcU7jSLOrhfp83yznBxYBZw4cOhWzhyLJiTPOZcDjkfITmEsouzdtGcKtkjw8AKUIvok2vPgFh5b3VOcz1/pkvdxJsqqmt81kmzV4kZa28W0qGxSj2H0yKWue2npG7pDn2TIpy6QrPljhXKTNBF8Htc3dVVpDz0jaMflNWpfbZkT9Xf8A44FhS6JpunND9glk/wCpJnPsrGPXhH+Spl3NjM2rpfwMVOpQUrQ2Ow/0tGE+MCvDBKb7FXawZYZABYgcouMUPWrxkivpXvlm8ztxcMn1RKRZkuK6LBgc5zHB2GYHr3XOQm14MzDGGxMsvnOxK5m5Ptj0bb0bx6JWCXHOhK6kYixbWSt7OXtud40by/BMs4D5VnZZdiWMBV2yAjOUmTBYw0pVghWDcQByTZSiG67NZpvwzSvgDqp7i9wuLYARxywujLzb2RS+HgzuqUTqCsfAb2GWk9Qnmnr5fdhYsHWXWOoG87ntb3KNPqwvCNVRDw6dtuRZeX3Ml50zJy/JszuqVmoR1ksdRI6M3uPMfpPb7L6Xqzx5sEckOrR5vKpQk4tWV/z9UMmYu81xd17W/wDascaFxgpfQvM75k2eSeO2f0xj+ilSot48bS6JUzXRFj22J6gAC/XthLXksKHQz4soG1ryRa178j7eiYiHiXkJFVVIJ/tTzfnPN/8A6VLgmjlFfobZrtfCRZxc084Bv/WUh6UZvtsP3IxXgDWyVGpaiauRpjp2MDWsHX1VvFiWGNI8/tbHOTUSbawNbtAwhnJS6KkMcrKauqxvcW2WRmdSo996ViePXVhdI0Ku1dwe1vhw9ZXDCCGKU3/A3a3sWDy7f6NPpvwbS0s3iVk/zDW5DNthf1VuGso+THz+r5MkeOONF5Cyjpbvp6eKM2tdosrChFPoz5Sy5KU3ZUu1CZ08lji6f4RdWCKigE08xjcHZByutBqERWxfIHOzkIXIN9LoYga07hbg2shchM20ShjDKtzWYzcLlI6Um42x5jTFT5ORlC59iXJOXRnYReFtl89zv5noJ+R+Bt4XD0VZS45ExD8mMrofD1GbHJuvY4snLEjZxSvGhiD6VWyPshjASGyArEmTBYZpQWCNUbS+eNreSQob6AyOomtkrXRhsbThoWLnnJukzNjiTti2s1tLNQH5iIOmGGO7K/6bsZGvbl4/YzBinGfXgy25a5rHIRuqGD1UydRZ0nUTVA7YR+i8psO81mU/LI/EOmUur0sb5gY6hjbMlZyPQ9wtXU9Y2NNrj3H9FKWKLl2YLUdNqaF9i/xGbgNzRwvYaHqsN20k1IVkxqCsQ+ccWtJuSRgH1vb+CvttkxioltqQ+TdA8v3RywCcPaOQefxe6r48nJssJRa6AeO4YFiW4sOp7ffkJ1sB0kR8V1gWncCMevuE5Ji+VCjdWc2qdTxuB2jzP/kpTqVFLZnyi1FF7p9W7aQXk5TrsyZY+JYDRptSqGvpniKEj9o49/RV5pWPwpJdotKP4c0yhl+YqCamUceJ9I9gqywQ5Wakt/POCxx6X8D8+psj2siDQBgAcJyEx1m+2K1GqOdGWjF11DoayTFnVTtm25NwotDVjV9kGMtFx5r5U8iW+yTmh9xfA6KGweVAxBYgi9roORPK0EaPDlePuosW+0glMA6rJ7BdZE+sZOsm2x7QclLcqAxQtlLSZhavBZ/zZ6GfksaMYIKqT8pleRmNeh2124DkL0+pkvEkaOtL4UAiGF02ObDtSWwQjUpshsK1BYJb/D8PiVYefpYMpebIoxtlfYdRLKtI8U7eiyW1KTYnGuis1IEwtdfkrU0YqNlnH+TK0laVlkPprd9W1BllUGBmdQNLL9DQvLydzbMywuoPEdKLkCwWhraWTayRhBdFXJlULkzI6hVXDw23v3X0b030vFpQ6Xy/Zg7O7LYnxj4M5W0zfEaYzty044FinTir6L2vmlx+XZZagyd+gaJNYu8Fj43NAvi/HtwFQxuKyyi/JoQVxcl9FRE7axrTnygE9bD6T7hWa7Bc6/5/df0F6yrkO5kdx/q6onKypkypdIUpmWeD/mOShXTEpto0VLMRuseXYTFKuxcsdujSUGp/LwNjac2uUtytl6GquKsnUahJK0DuusfDDGJAHFyhsL+gRm3/ABFdZHZJp2klubIWyHG/I00btrvyo5UIbp0SEdpTYYK7kRytBZLNjsLEoG6AirYKON0rwR9RS3N/QyTUV2TewU+631Oyo9xx8AqXueRVjS9znPz2CC3LyTKXHpFfQHdEPReK2VU2b0/JZ0eH2VOfgRNdFR8SwWLXjoVsaGT4UP1ZfRUMGFblLstthWpTZARqW2QECCyDUaOwQ0Fx9T8krK3ZuWTj9FLK+UyFQblLxIKInXEfKAHoVqazqVDcf5sq7ghX0yyPaK28+6yVtSrGI2H8S7lkax7XOPlbysXU1p58nGJnzkoxbZQa3q4qpDHGSGDGOq+lemaWPVgv2eW288s0uMfBQzSHN+FoZMtIZr66/QjUyGzlWi+asu5P8OkgbNanbpb9PNyDKHtff6R2SVji8nP7Ollmo0vsSEsj5GWuSTwE5+BHKTZaO0tr3iWa4FvpSeVFyGu5dsBWMYI7xiwjN8JTmW5a6UOgmnu3xMf0ubD1UrJYGLBb5MuKfdyTzhcpFpsdjbxc8KbFth5cbey7kRAYDA5rSF1g32MRtaGnCixTbs7E6wwVDkiGgxeS3H5S5T/QPBWdhaXC7jhBbfkGcuPgI94pXHNw7hdfECvcFvH8SY7wRYYv1Q2TKNR6PEtF+ULkLpsp9KdujyvI7iqZ6bKuy2pzteCFQl4K8gevQ+JTEgK3pTpnYHUjNMGM8rSlLs0GySBsgm1LkzgrUFkGro/3OL/tWRn/AMxlGX5MBPym4Q4iGpYpmkdSr2F/4g3H+bKlhxlaJaRdaI02uqe5L4FPYf0C11s08ngwuLRa5K3f/wA9pL2vca8nmfVtr26gZytgmoo7yXIPUL1ElwjZn63Gb6ARhz2b38Lzu/v/AOiJ6DX16VsTqCtP09t4UU9380BoNKq9Rn2U0Z2jmQjyge6bT5AWqNNFp1HpMfIkqLZepkyxg135K2oqHSuOcKvJmnGCigAaDylhMNCGtNgAOy4FobjcRgHK7kA0PwvBNjyp5C2hsWLcrlIFBIpbYPRRzSOlEK1znHHBQPJ+gGkgsUdxnuoTsCU6GmFsbHNIueQusU032iEDiPK8WHRDyRORX2j1Q9rpmgWuFDlbFxtRYGfH7Qn6VDZ0H/pICfxGG3HZLkzuPF0UuivuAF5nc7dnpcqLyPos1ldjdUzxaV3spwT4yErqRkJGbJHD1WryNFPo4AociSbcIDiY5HuoIZq6T90j9lk5fzZSl+QKblWMAcRDUhelPocK1jdTDxv5FQ0ZV/kWrNHpDNsN1S2nyaiUc0uyurqt0lW5kTSbHovofpuFYdaMV+jw3qU3lzu/ohNSSVMG120nm10/Zi5Yml5D0WoZFYkNLqql3hU8DnWxcfSPuvEQ09meRrieqexijG2w7Ph6hpLSapUtkcP+Uw4+5Xq9XG8ONRZm5FLYl8V0EqNTjjj+Xoo2xxDiw5RymvotYdVR7kUtS9xJLnXukylZej10Jk9klsI80gcobOomDc46KORDQzE4bgosGhxrtha7qucgRhs+MIXNEcQsYLvNdLu2C2OwG2eiK0Jl2MiVuNowOSo5UIcf2cmqACwjJvmyFzJUTk1nRk7ju5QciF0wZOxp2/Uocjn26YMuLm7XHCiWRJEJUcaCMNVaedvpElJo52vA9Vj7PaPSZfBpWfSFlyKrHWeaIj0S7piJeTMarD4dUT3WninyiXMTuIoAmDSSg4k36vuF30Q/Bq6b92Z7LJn+bKT/ACBy8qxrhoTqhenIVhfkHH8ioY27gO6uJlhvo09DE75cBrSbDoFUcJ5c0YxX2Z2aaXZnKmrbFPI1gMZ3G5PdfTcK444o8fmjyyyb/YFla5rxm4TJPo7HCpWz1Zr1e0fLteI4QMBotcLOyZ5RlR6LW1sc4KfkrTUFxu5xJPc3SfdsvcaImboFHIniCe9RZNAt+UDZJ0CyBs4kHWKGzgjZSHDaociKGmyE23oLIociGLqLFsaDwNqixbQaOQuuBwusBqghm2MLW8oXLoHir7JRP8pB5QuXQMvJJpN8lKlkSAaO9SlPK5eCKOGwQ8ZPyQ2DdJ0GPZNhBIFspNP8k7VkZu0emn4NPTm8YWVLyVH5G6dKkLkiq1yG7S4dFa1p/QzFKilCustElBxJn1D3C76I+jU037u1ZU/zKb8kXtLnbQLnsrOvFt0grX2Fh0iqqmnyiNp/xOWxr+l7GZ2+l/Ime1jh/ISPR9L0476qZ08ozYcLdxemYca+fYl59jN1BUdqNbLGGOkhZEwcHqrsfaxqoo6Ok27yO2Y3Wo3SPdUMBLnG7vfum49pJ0xO36epLlBFVHUHdzut9Q/mrKyfaMt4u6ZKpeJIbg3sLtKq7SUlyL+hJxlwYl4ipJmw0d8TKKwSDX5N11nEt9uEDZx7xFDZ1Ehc5shOCt8uULZA02z2cZQ2CMRSWIv0GChbIYdp3OuVFgMYjkIwBZQ5C2FabclKeVIBhmEbuUiWVy6QBPc0coVG/ILZ3cXeW2E1JIU2ccEywLAPefqHPClEsqKc2kaSsafg9OzTURvGFl5F2VZeRxlwUpgMhXxCSBynFKmRB0zMvbteW9lqJ2rLaIriScYJeABckrqvpEPpGx0+jLqZrpXbGput6Pkzz5T6RnZMtOohX19FReWFrXvXpdfT19ZVFdgrBly9ydIQqtXnnuDJsb/lCsSzV4LOPUxxK6SpzkpEszLKxqhWWo7FKllYXARnmve/ZJeRsjiU9XE0kuadrvRPxbEkVcupCYi4zNcQD5Sbnsnyz8lRXhquErRwuS0y2z25EQdabnK4gIAhZx04GBdC2cEDrhBZDJx2v3UNnDMRceEtsBh2IOSBDsKBzAYZhPVKcmwWHa63qg42LbCBxOQMIlSFthP8Nz3U2KsmXNFrHldfZFfsi8udwLJhCaQrI/aNgyb5RJh8V5K+MZCx5HomaHTnXYPZZ+ZdleZYNVZi6JvG6MhQumCZ3UY9k24cFaWGVosQdqhSyaML/wCHKFkh8aQDGRdbPpmupfORS2sj/FD2rVR2mNpLWjstjJPj0gtXCvLKIvIN7qq8ho11QKSUpMpk8UAfKT1SZZCaBOkxlL9wihWZ91ykC0IzOTYsWxR5T4sUwDimoFngUVgk2kjKhs4mO6GyAjblC5HWEa1LciArAByluZDYZvoltgMK11kDtg2Fa5RSBYZpuMqG6AYxGQO6hsWwzOLBCLbCDmx4RIC/0d2gC4uSiRC78hB9O5MbArsDHH+0LiMFQpKg3fhFS1ZbPRl3phO0KhnEzLVvCqsUEHCAFlPq4FvuruuxuMqv91c+xpsdDaPlOOi9LodYjM2P8wqtUcfEcjzM09dfErnFVJMtC8pwkthC5JSpMkG8myVYti0hNkyIDFJeFYgLYs9WIimDKagTgUkEwoZAVqW2QwgS2yAjUBAQKAWSaUDBYRpUAsM3hLYLGIlADGWKBYeNEhcgh+pEiIk48FSiH5PS4aLJWRtDIJNkWMBte6mHyfZMuvB//9k=
)

![Alt text]([https://example.com/image.jpg](https://private-user-images.githubusercontent.com/44409029/253736667-f7931af3-d4c2-4ca0-bf00-d09e2c18e313.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MTgxMTEzMTIsIm5iZiI6MTcxODExMTAxMiwicGF0aCI6Ii80NDQwOTAyOS8yNTM3MzY2NjctZjc5MzFhZjMtZDRjMi00Y2EwLWJmMDAtZDA5ZTJjMThlMzEzLnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNDA2MTElMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjQwNjExVDEzMDMzMlomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTk4MDFjYmZlNWY1MmYzNjkwMGRkODZlNGExMmYwZGQyMGZkMjc3MmZhZTZlYWUyZWJlNzNlMTEzNzVkY2ZlYjUmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0JmFjdG9yX2lkPTAma2V5X2lkPTAmcmVwb19pZD0wIn0.O7WdzNFyHNpHsjIIQzMaI4TovjCrYAvcfcJoMvW6gS4](https://private-user-images.githubusercontent.com/44409029/253736650-466e8a7e-b610-41c9-bfdb-5291465f24e4.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MTgxMTEzMTIsIm5iZiI6MTcxODExMTAxMiwicGF0aCI6Ii80NDQwOTAyOS8yNTM3MzY2NTAtNDY2ZThhN2UtYjYxMC00MWM5LWJmZGItNTI5MTQ2NWYyNGU0LnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNDA2MTElMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjQwNjExVDEzMDMzMlomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPWYyYTlmNzExOTYzYzE1MDdiNGYxZDdjYmJiMTk0YTdmY2ZhODAwNGJlNmMwYzQ4NDI3ZGY5YTBlMTY4YThmZWYmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0JmFjdG9yX2lkPTAma2V5X2lkPTAmcmVwb19pZD0wIn0.rgZXXbL5IyD5LC0Vx2nISVOajqfANbl9eNbRh8Kqr14)
)



 


