from instagrapi import Client

cl = None


def instagram_comment_removal():
    global cl
    try:
        ig_account = 'ig_profile_name'
        ig_pass = 'ig_password'
        
        cl = Client()
        cl.login(ig_account, ig_pass)

        user_id = cl.user_id_from_username(ig_account)
        medias = cl.user_medias(int(user_id), 3)  # three last posts

        posts_with_comments = [post for post in medias if post.comment_count]
        for post in posts_with_comments:
            post_comments = cl.media_comments(post.pk)
            bad_words = ['crypto', 'pito']
            bad_comments = [comment for comment in post_comments if any(word in comment.text.lower() for word in bad_words)]
            if bad_comments:
                cl.comment_bulk_delete(post.pk, [int(c.pk) for c in bad_comments])
    except Exception as ex:
        print(ex)
    finally:
        cl.logout()


if __name__ == "__main__":
    instagram_comment_removal()
