class Solution:
    def readBinaryWatch(self, num: int) -> List[str]:
        if num == 0:
            return ['0:00']
        if num == 1:
            return ['0:01', '0:02', '0:04', '0:08', '0:16', '0:32', '1:00', '2:00', '4:00', '8:00']
        if num == 2:
            return ['0:03', '0:05', '0:09', '0:17', '0:33', '1:01', '2:01', '4:01', '8:01', '0:06', '0:10', '0:18',
                    '0:34', '1:02', '2:02', '4:02', '8:02', '0:12', '0:20', '0:36', '1:04', '2:04', '4:04', '8:04',
                    '0:24', '0:40', '1:08', '2:08', '4:08', '8:08', '0:48', '1:16', '2:16', '4:16', '8:16', '1:32',
                    '2:32', '4:32', '8:32', '3:00', '5:00', '9:00', '6:00', '10:00']
        if num == 3:
            return ['0:07', '0:11', '0:19', '0:35', '1:03', '2:03', '4:03', '8:03', '0:13', '0:21', '0:37', '1:05',
                    '2:05', '4:05', '8:05', '0:25', '0:41', '1:09', '2:09', '4:09', '8:09', '0:49', '1:17', '2:17',
                    '4:17', '8:17', '1:33', '2:33', '4:33', '8:33', '3:01', '5:01', '9:01', '6:01', '10:01', '0:14',
                    '0:22', '0:38', '1:06', '2:06', '4:06', '8:06', '0:26', '0:42', '1:10', '2:10', '4:10', '8:10',
                    '0:50', '1:18', '2:18', '4:18', '8:18', '1:34', '2:34', '4:34', '8:34', '3:02', '5:02', '9:02',
                    '6:02', '10:02', '0:28', '0:44', '1:12', '2:12', '4:12', '8:12', '0:52', '1:20', '2:20', '4:20',
                    '8:20', '1:36', '2:36', '4:36', '8:36', '3:04', '5:04', '9:04', '6:04', '10:04', '0:56', '1:24',
                    '2:24', '4:24', '8:24', '1:40', '2:40', '4:40', '8:40', '3:08', '5:08', '9:08', '6:08', '10:08',
                    '1:48', '2:48', '4:48', '8:48', '3:16', '5:16', '9:16', '6:16', '10:16', '3:32', '5:32', '9:32',
                    '6:32', '10:32', '7:00', '11:00']
        if num == 4:
            return ['0:15', '0:23', '0:39', '1:07', '2:07', '4:07', '8:07', '0:27', '0:43', '1:11', '2:11', '4:11',
                    '8:11', '0:51', '1:19', '2:19', '4:19', '8:19', '1:35', '2:35', '4:35', '8:35', '3:03', '5:03',
                    '9:03', '6:03', '10:03', '0:29', '0:45', '1:13', '2:13', '4:13', '8:13', '0:53', '1:21', '2:21',
                    '4:21', '8:21', '1:37', '2:37', '4:37', '8:37', '3:05', '5:05', '9:05', '6:05', '10:05', '0:57',
                    '1:25', '2:25', '4:25', '8:25', '1:41', '2:41', '4:41', '8:41', '3:09', '5:09', '9:09', '6:09',
                    '10:09', '1:49', '2:49', '4:49', '8:49', '3:17', '5:17', '9:17', '6:17', '10:17', '3:33', '5:33',
                    '9:33', '6:33', '10:33', '7:01', '11:01', '0:30', '0:46', '1:14', '2:14', '4:14', '8:14', '0:54',
                    '1:22', '2:22', '4:22', '8:22', '1:38', '2:38', '4:38', '8:38', '3:06', '5:06', '9:06', '6:06',
                    '10:06', '0:58', '1:26', '2:26', '4:26', '8:26', '1:42', '2:42', '4:42', '8:42', '3:10', '5:10',
                    '9:10', '6:10', '10:10', '1:50', '2:50', '4:50', '8:50', '3:18', '5:18', '9:18', '6:18', '10:18',
                    '3:34', '5:34', '9:34', '6:34', '10:34', '7:02', '11:02', '1:28', '2:28', '4:28', '8:28', '1:44',
                    '2:44', '4:44', '8:44', '3:12', '5:12', '9:12', '6:12', '10:12', '1:52', '2:52', '4:52', '8:52',
                    '3:20', '5:20', '9:20', '6:20', '10:20', '3:36', '5:36', '9:36', '6:36', '10:36', '7:04', '11:04',
                    '1:56', '2:56', '4:56', '8:56', '3:24', '5:24', '9:24', '6:24', '10:24', '3:40', '5:40', '9:40',
                    '6:40', '10:40', '7:08', '11:08', '3:48', '5:48', '9:48', '6:48', '10:48', '7:16', '11:16', '7:32',
                    '11:32']
        if num == 5:
            return ['0:31', '0:47', '1:15', '2:15', '4:15', '8:15', '0:55', '1:23', '2:23', '4:23', '8:23', '1:39',
                    '2:39', '4:39', '8:39', '3:07', '5:07', '9:07', '6:07', '10:07', '0:59', '1:27', '2:27', '4:27',
                    '8:27', '1:43', '2:43', '4:43', '8:43', '3:11', '5:11', '9:11', '6:11', '10:11', '1:51', '2:51',
                    '4:51', '8:51', '3:19', '5:19', '9:19', '6:19', '10:19', '3:35', '5:35', '9:35', '6:35', '10:35',
                    '7:03', '11:03', '1:29', '2:29', '4:29', '8:29', '1:45', '2:45', '4:45', '8:45', '3:13', '5:13',
                    '9:13', '6:13', '10:13', '1:53', '2:53', '4:53', '8:53', '3:21', '5:21', '9:21', '6:21', '10:21',
                    '3:37', '5:37', '9:37', '6:37', '10:37', '7:05', '11:05', '1:57', '2:57', '4:57', '8:57', '3:25',
                    '5:25', '9:25', '6:25', '10:25', '3:41', '5:41', '9:41', '6:41', '10:41', '7:09', '11:09', '3:49',
                    '5:49', '9:49', '6:49', '10:49', '7:17', '11:17', '7:33', '11:33', '1:30', '2:30', '4:30', '8:30',
                    '1:46', '2:46', '4:46', '8:46', '3:14', '5:14', '9:14', '6:14', '10:14', '1:54', '2:54', '4:54',
                    '8:54', '3:22', '5:22', '9:22', '6:22', '10:22', '3:38', '5:38', '9:38', '6:38', '10:38', '7:06',
                    '11:06', '1:58', '2:58', '4:58', '8:58', '3:26', '5:26', '9:26', '6:26', '10:26', '3:42', '5:42',
                    '9:42', '6:42', '10:42', '7:10', '11:10', '3:50', '5:50', '9:50', '6:50', '10:50', '7:18', '11:18',
                    '7:34', '11:34', '3:28', '5:28', '9:28', '6:28', '10:28', '3:44', '5:44', '9:44', '6:44', '10:44',
                    '7:12', '11:12', '3:52', '5:52', '9:52', '6:52', '10:52', '7:20', '11:20', '7:36', '11:36', '3:56',
                    '5:56', '9:56', '6:56', '10:56', '7:24', '11:24', '7:40', '11:40', '7:48', '11:48']
        if num == 6:
            return ['1:31', '2:31', '4:31', '8:31', '1:47', '2:47', '4:47', '8:47', '3:15', '5:15', '9:15', '6:15',
                    '10:15', '1:55', '2:55', '4:55', '8:55', '3:23', '5:23', '9:23', '6:23', '10:23', '3:39', '5:39',
                    '9:39', '6:39', '10:39', '7:07', '11:07', '1:59', '2:59', '4:59', '8:59', '3:27', '5:27', '9:27',
                    '6:27', '10:27', '3:43', '5:43', '9:43', '6:43', '10:43', '7:11', '11:11', '3:51', '5:51', '9:51',
                    '6:51', '10:51', '7:19', '11:19', '7:35', '11:35', '3:29', '5:29', '9:29', '6:29', '10:29', '3:45',
                    '5:45', '9:45', '6:45', '10:45', '7:13', '11:13', '3:53', '5:53', '9:53', '6:53', '10:53', '7:21',
                    '11:21', '7:37', '11:37', '3:57', '5:57', '9:57', '6:57', '10:57', '7:25', '11:25', '7:41', '11:41',
                    '7:49', '11:49', '3:30', '5:30', '9:30', '6:30', '10:30', '3:46', '5:46', '9:46', '6:46', '10:46',
                    '7:14', '11:14', '3:54', '5:54', '9:54', '6:54', '10:54', '7:22', '11:22', '7:38', '11:38', '3:58',
                    '5:58', '9:58', '6:58', '10:58', '7:26', '11:26', '7:42', '11:42', '7:50', '11:50', '7:28', '11:28',
                    '7:44', '11:44', '7:52', '11:52', '7:56', '11:56']
        if num == 7:
            return ['3:31', '5:31', '9:31', '6:31', '10:31', '3:47', '5:47', '9:47', '6:47', '10:47', '7:15', '11:15',
                    '3:55', '5:55', '9:55', '6:55', '10:55', '7:23', '11:23', '7:39', '11:39', '3:59', '5:59', '9:59',
                    '6:59', '10:59', '7:27', '11:27', '7:43', '11:43', '7:51', '11:51', '7:29', '11:29', '7:45',
                    '11:45', '7:53', '11:53', '7:57', '11:57', '7:30', '11:30', '7:46', '11:46', '7:54', '11:54',
                    '7:58', '11:58']
        if num == 8:
            return ['7:31', '11:31', '7:47', '11:47', '7:55', '11:55', '7:59', '11:59']
        if num >= 9:
            return []
