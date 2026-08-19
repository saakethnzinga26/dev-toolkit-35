import sys
def process_data(data):
    if not isinstance(data, str) or not data:
        raise ValueError('Invalid input: Data must be a non-empty string.')
    return data.upper()

def main_loop():
    while True:
        try:
            user_input = input('Enter some data (or type "exit" to quit): ')
            if user_input.lower() == 'exit':
                print('Exiting...')
                break
            processed = process_data(user_input)
            print(f'Processed data: {processed}')
        except ValueError as e:
            print(e)
        except KeyboardInterrupt:
            print('\nInterrupted. Exiting...')
            break

if __name__ == '__main__':
    main_loop()