# JPA 문법

## JPA 조회 예시

```java

public interface BotBoardRepository extends JpaRepository<BotBoard, Long> {
    Optional<BotBoard> findByArticleId(String articleId);
}

public interface RssMediaRepository extends JpaRepository<RssMedia, Long> {
    List<RssMedia> findByName(String name);

    @Query("SELECT rm FROM RssMedia rm WHERE rm.name LIKE %:name%")
    List<RssMedia> searchByNameLike(String name);
}

public interface UserRepository extends JpaRepository<User, Integer> {
    boolean existsByUserId(String userId);

    @Query("SELECT u FROM User u WHERE u.userId = :user_id AND u.userPwd = :user_pwd")
    List<User> findByUserIdAndPwd(@Param("user_id") String userId, @Param("user_pwd") String userPwd);

    Optional<User> findByUserId(String userId);
    Optional<User> findOneWithAuthoritiesByUserId(String userId);
}

```

## JPA Save 예시
``` java

@Transactional
public User signup(User user) {
    if (userRepository.findOneWithAuthoritiesByUserId(user.getUserId()).orElse(null) != null) {
        throw new RuntimeException("이미 가입되어 있는 회원입니다.");
    }

    Optional<Authority> authority = authorityRepository.findByName("ROLE_USER");
    User newUser = User.builder()
            .userId(user.getUserId())
            .userPwd(passwordEncoder.encode(user.getUserPwd()))
            .name(user.getName())
            .mail(user.getMail())
            .sex(user.getSex())
            .birth(user.getBirth())
            .active(true)
            .delete(false)
            .signupDate(DateTimeUtil.getCurrentDateTimeKRFromLocalDateTime())
            .authorities(Collections.singleton(authority.get()))
            .build();

    User userResult = userRepository.save(newUser);
    return userResult;
}

```

