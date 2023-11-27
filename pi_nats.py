import asyncio
import nats
import json

async def main():
    async def disconnected_cb():
        print('Got disconnected!')

    async def reconnected_cb():
        print(f'Got reconnected to {nc.connected_url.netloc}')

    async def error_cb(e):
        print(f'There was an error: {e}')

    async def closed_cb():
        print('Connection is closed')

    # Connect to NATS with logging callbacks.
    nc = await nats.connect('0.0.0.0:4222',
                             error_cb=error_cb,
                             reconnected_cb=reconnected_cb,
                             disconnected_cb=disconnected_cb,
                             closed_cb=closed_cb,
                             )

    async def handler(msg):
        print(f'Received a message on {msg.subject} {msg.reply}: {msg.data}')
        location_data = json.loads(msg.data.decode())
        print(location_data)
        await msg.respond(b'OK')

    sub = await nc.subscribe('location.please', cb=handler)

    resp = await nc.request('location.please', json.dumps({'lat': 123, 'lon': 456}).encode(), timeout=1)
    print('Response:', resp)

    await nc.close()

if __name__ == '__main__':
    asyncio.run(main())