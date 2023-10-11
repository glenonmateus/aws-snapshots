import boto3
import snapshots
import json
import csv

client = boto3.client('ec2', region_name='us-east-1')
#
# images = client.describe_images(
#     Filters=[
#         {
#             'Name': 'name',
#             'Values': [
#                 'Backup*'
#             ]
#         },
#     ],
#     Owners=[
#         'self'
#     ],
# )
# for snapshot in snapshots_ids:
#     try:
#         response = client.describe_snapshots(
#             SnapshotIds=[snapshot]
#         )
#         print(response)
#     except Exception as e:
#         print('Snapshot não encontrado %s' % snapshot)


def image_sort(elem, sort='CreationDate'):
    return elem.get(sort)


def getAMIs(filter={'Name': 'name', 'Values': []}, owners=['self'], region='us-east-1'):
    client = boto3.client('ec2', region_name=region)
    response = client.describe_images(
        Filters=[
            filter
        ],
        Owners=owners
    )
    return response['Images']


def main():
    client = boto3.client('ec2', region_name='us-east-1')
    response = client.describe_images(
        Owners=['self']
        # Filters=[
        #     {
        #         'Name': 'name',
        #         'Values': [
        #             ...
        #         ]
        #     }
        # ]
    )
    amis = response.get('Images')
    amis.sort(key=image_sort)
    print(amis)


if __name__ == "__main__":
    main()
    # images = images.get('Images')
    # images.sort(key=image_sort)
    # images_info = []
    #
    # for image in images[:-2]:
    #     for device_map in image['BlockDeviceMappings']:
    #         if 'Ebs' in device_map:
    #             images_info.append({
    #                 'ImageId': image['ImageId'],
    #                 'SnapshotId': device_map['Ebs']['SnapshotId']
    #             })
    #
    # for image in images_info:
    #     print(image)
    #
    # with open('images_info.txt', 'w') as file:
    #     json.dump(images_info, file)

    # with open('images_info.csv', 'w', newline='') as file:
    #     writer = csv.DictWriter(file, fieldnames=images_info[0].keys())
    #     writer.writeheader()
    #     for image in images_info:
    #         writer.writerow(image)

    # for image in images_info:
    #     image_id = image['ImageId']
    #     snapshot_id = image['SnapshotId']
    #     if snapshot_id in snapshots.getSnapshots():
    #         print('Deregistering image ... ' + image_id)
    #         response = client.deregister_image(
    #             ImageId=image['ImageId']
    #         )
    #         print('Deleting snapshot ... ' + image_id)
    #         response = client.delete_snapshot(
    #             SnapshotId=image['SnapshotId']
    #         )
