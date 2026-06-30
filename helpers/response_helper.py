class ResponseHelper:

    @staticmethod
    def success(data):

        return {
            "success": True,
            "data": data,
        }
