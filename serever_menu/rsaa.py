import rsa
import pickle
pubkey, privkey = rsa.newkeys(4096)  # генерируем пару ключей
# pickle.dump(privkey, open('client_private.key', 'wb+'))  # сохраняем ключ в файл
# pickle.dump(pubkey, open('client_public.key', 'wb+'))  # сохраняем ключ в файл
pickle.dump(privkey, open('server_private.key', 'wb+'))  # сохраняем ключ в файл
pickle.dump(pubkey, open('server_public.key', 'wb+'))  # сохраняем ключ в файл