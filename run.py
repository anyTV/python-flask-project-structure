from app import app

import sys


if len(sys.argv) > 1:
    app.run(host='0.0.0.0', port=int(sys.argv[1]), threaded=True)

else:
    app.run(host='0.0.0.0', port=3000, threaded=True)
