// 1. Import the "HttpResponse" class from the library.
import { http, HttpResponse } from 'msw';

export const handlers = [
  http.get('/resource', () => {
    // 2. Return a mocked "Response" instance from the handler.
    return HttpResponse.text('Hello world!');
  }),

  http.get('/name', () => {
    return new HttpResponse('John');
  }),

  http.post('/login', ({ request }) => {
    if (!request.headers.has('cookie')) {
      throw new HttpResponse(null, { status: 400 });
    }
  }),

  http.get('/apples', () => {
    return new HttpResponse(null, {
      status: 404,
      statusText: 'Out Of Apples'
    });
  }),

  http.post('/auth', () => {
    // Note that you DON'T have to stringify the JSON!
    return HttpResponse.json({
      user: {
        id: 'abc-123',
        name: 'John Maverick'
      }
    });
  })
];
