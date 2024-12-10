from django.http import JsonResponse
import traceback
import logging

logger = logging.getLogger(__name__)

def custom_exception_middleware(get_response):
    def middleware(request):
        try:
            response = get_response(request)
            if response.status_code != 200:
                # Adicionar detalhes sobre a URL e método da requisição
                logger.error(f'Error: {response.status_code} - {response.reason_phrase} at {request.method} {request.path}')
                return JsonResponse({'error': 'An error occurred', 'details': response.reason_phrase}, status=response.status_code)
            return response
        except Exception as e:
            tb = traceback.format_exc()
            logger.error(f'Unexpected Error: {str(e)} - {tb}')
            return JsonResponse({'error': 'An unexpected error occurred', 'details': str(e), 'traceback': tb}, status=500)

    return middleware
