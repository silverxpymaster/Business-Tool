import os
import time
from termcolor import colored
from telethon.sync import TelegramClient
from telethon.tl.functions.messages import ImportChatInviteRequest
import sys

print(colored(r"""
    ____             _                          ______            __   
   / __ )__  _______(_)___  ___  __________    /_  __/___  ____  / /   
  / __  / / / / ___/ / __ \/ _ \/ ___/ ___/_____/ / / __ \/ __ \/ /    
 / /_/ / /_/ (__  ) / / / /  __(__  |__  )_____/ / / /_/ / /_/ / /     
/_____/\__,_/____/_/_/ /_/\___/____/____/     /_/  \____/\____/_/      

              
           ⣀⣤⣴⣶⣶⣶⣶⣦⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣀⣤⣾⣿⡿⠿⠛⠛⠛⠛⠛⠛⠻⢿⣿⣿⣦⣄⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢠⣼⣿⡿⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠿⣿⣷⣄⠀⠀⠀⠀
⠀⠀⠀⣰⣿⡿⠋⠀⠀⠀⠀⠀⣿⡇⠀⢸⣿⡇⠀⠀⠀⠀⠀⠈⢿⣿⣦⡀⠀⠀
⠀⠀⣸⣿⡿⠀⠀⠀⠸⠿⣿⣿⣿⡿⠿⠿⣿⣿⣿⣶⣄⠀⠀⠀⠀⢹⣿⣷⠀⠀
⠀⢠⣿⡿⠁⠀⠀⠀⠀⠀⢸⣿⣿⡇⠀⠀⠀⠈⣿⣿⣿⠀⠀⠀⠀⠀⢹⣿⣧⠀
⠀⣾⣿⡇⠀⠀⠀⠀⠀⠀⢸⣿⣿⡇⠀⠀⢀⣠⣿⣿⠟⠀⠀⠀⠀⠀⠈⣿⣿⠀
⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⢸⣿⣿⡿⠿⠿⠿⣿⣿⣥⣄⠀⠀⠀⠀⠀⠀⣿⣿⠀
⠀⢿⣿⡇⠀⠀⠀⠀⠀⠀⢸⣿⣿⡇⠀⠀⠀⠀⢻⣿⣿⣧⠀⠀⠀⠀⢀⣿⣿⠀
⠀⠘⣿⣷⡀⠀⠀⠀⠀⠀⢸⣿⣿⡇⠀⠀⠀⠀⣼⣿⣿⡿⠀⠀⠀⠀⣸⣿⡟⠀
⠀⠀⢹⣿⣷⡀⠀⠀⢰⣶⣿⣿⣿⣷⣶⣶⣾⣿⣿⠿⠛⠁⠀⠀⠀⣸⣿⡿⠀⠀
⠀⠀⠀⠹⣿⣷⣄⠀⠀⠀⠀⠀⣿⡇⠀⢸⣿⡇⠀⠀⠀⠀⠀⢀⣾⣿⠟⠁⠀⠀
⠀⠀⠀⠀⠘⢻⣿⣷⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣾⣿⡿⠋⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠈⠛⢿⣿⣷⣶⣤⣤⣤⣤⣤⣤⣴⣾⣿⣿⠟⠋⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠛⠻⠿⠿⠿⠿⠟⠛⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
      
        
        Author: SilverX            TG Channel: t.me/silverxvip
      """,'yellow'))



def graceful_exit():
    print("\nProqram dayandirildi..")
    sys.exit(0)

def run_program():
    session_name = 'session'
    group_file = "groups.txt"

    try:
        session_exists = os.path.exists(f"{session_name}.session")

        if not session_exists:
            try:
                api_id = int(input("Telegram API ID daxil et: ").strip())
                api_hash = input("Telegram API HASH daxil et: ").strip()
                phone_number = input("Telefon nömrəsini daxil et (+994 ilə): ").strip()
            except KeyboardInterrupt:
                graceful_exit()
            except Exception as e:
                print(f"\n[Xəta] Giriş zamanı xəta baş verdi: {e}")
                graceful_exit()

            client = TelegramClient(session_name, api_id, api_hash)
            try:
                client.start(phone_number)
            except Exception as e:
                print(f"\n[Xəta] Telegram bağlantısı qurularkən xəta: {e}")
                graceful_exit()
        else:
            api_id = 12345
            api_hash = '0123456789abcdef0123456789abcdef'
            client = TelegramClient(session_name, api_id, api_hash)

        async def main():
            try:
                await client.start()
                print("\n[✔] Bot başladı və işləyir...\n")

                if os.path.exists(group_file):
                    try:
                        secim = input(f"\n'{group_file}' tapildi. İstifade etmek isteyirsen? (yes/no): ").strip().lower()
                        if secim == 'yes':
                            with open(group_file, 'r') as f:
                                groups = [line.strip() for line in f if line.strip()]
                        else:
                            groups = await qrup_yig()
                    except KeyboardInterrupt:
                        graceful_exit()
                else:
                    groups = await qrup_yig()

                with open(group_file, 'w') as f:
                    for group in groups:
                        f.write(group + '\n')

                try:
                    post_link = input("\nGönderilecek post linkini daxil et (məs: https://t.me/kanal/43): ").strip()
                    interval = int(input("Neçe deqiqeden bir gönderilsin?: "))
                except KeyboardInterrupt:
                    graceful_exit()
                except ValueError:
                    print("\n[Xəta] Deqiqe sayi reqem olmalidir!")
                    graceful_exit()

                if "t.me/" in post_link:
                    try:
                        parts = post_link.replace("https://", "").replace("http://", "").split('/')
                        if len(parts) < 3:
                            print("[Xeta] Link tam deyil! Zehmet olmasa düzgün link daxil edin")
                            return
                        channel_username = parts[1]
                        message_id = int(parts[2])
                    except Exception as e:
                        print(f"[Xeta] Linki istifade etmek alinmadi: {e}")
                        return
                else:
                    print("[Xeta] Link düzgün formatda deyil!")
                    return

                while True:
                    try:
                        for group in groups:
                            try:
                                if "joinchat" in group and "+" in group:
                                    invite_hash = group.split("+")[1]
                                    await client(ImportChatInviteRequest(invite_hash))
                                    entity = await client.get_entity(group)
                                else:
                                    entity = await client.get_entity(group)

                                from_channel = await client.get_entity(channel_username)
                                await client.forward_messages(entity, message_id, from_channel)

                                print(f"[✔] Post gönderildi: {group}")

                            except Exception as e:
                                print(f"[Xeta] {group} üçün: {e}")

                        print(f"\n{interval} deqiqe gözlenilir...\n")
                        time.sleep(interval * 60)
                    except KeyboardInterrupt:
                        graceful_exit()
                    except Exception as e:
                        print(f"\n[Ümumi xeta] {e}")
                        time.sleep(10)

            except Exception as e:
                print(f"\n[Əsas funksiyada xeta] {e}")
                graceful_exit()

        async def qrup_yig():
            print("\nQrup linklerini daxil et. Bitirmek üçün 'q' yaz")
            groups = []
            while True:
                try:
                    link = input("Qrup linki: ").strip()
                    if link.lower() == 'q':
                        break
                    if link:
                        groups.append(link)
                except KeyboardInterrupt:
                    graceful_exit()
                except Exception as e:
                    print(f"\n[Qrup yığanda xəta] {e}")
                    continue
            return groups

        with client:
            client.loop.run_until_complete(main())

    except KeyboardInterrupt:
        graceful_exit()
    except Exception as e:
        print(f"\n[Ümumi proqram xetasi] {e}")
        graceful_exit()

if __name__ == "__main__":
    try:
        run_program()
    except KeyboardInterrupt:
        graceful_exit()
    except Exception as e:
        print(f"\n[Proqram başladmaqda xeta yarandi] {e}")
        graceful_exit()
